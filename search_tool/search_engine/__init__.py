from search_tool.search_engine.database import Document


class SearchEngine:
    def __init__(self, crawler, indexer, filesystem, query_processor):
        self.crawler = crawler
        self.indexer = indexer
        self.filesystem = filesystem
        self.query_processor = query_processor
        self.inverted_index = {}

    def build_inverted_index(self):
        inverted_index = {}

        document_database = Document()

        self.crawler.crawl(document_database)

        for document_entry in document_database.all():
            texts = self.crawler.parser.extract_visible_text(document_entry)

            inverted_index = self.indexer.generate_index(document_entry['id'], texts)

        # Save to the filesystem
        self.filesystem.save('inverted_index.json', inverted_index)
        self.filesystem.save('database.json', document_database.all())

    def load_inverted_index(self):
        self.inverted_index = self.filesystem.get('inverted_index.json')

    def get_inverted_index_for_term(self, term):
        inverted_index = {}

        if term not in self.inverted_index:
            return inverted_index

        inverted_index = self.inverted_index[term]

        return inverted_index

    def find_documents(self, query):
        documents = []
        terms = self.query_processor.process(query)

        matches = []
        for term in terms:
            if term not in self.inverted_index:
                return documents

            matches.append(set([appearance['document_id'] for appearance in self.inverted_index[term]]))

        document_ids = set.intersection(*matches)

        filtered_index = {}

        for term in terms:
            filtered_index[term] = list(
                filter(lambda appearance: appearance['document_id'] in document_ids, self.inverted_index[term]))

        return self.rank_documents(terms, filtered_index)

    def rank_documents(self, terms, filtered_index):
        documents = []
        document_database = Document()
        ranks = {}
        for term in terms:
            for appearance in filtered_index[term]:
                if appearance['document_id'] not in ranks:
                    ranks[appearance['document_id']] = appearance['frequency']
                else:
                    ranks[appearance['document_id']] += appearance['frequency']

        for document_id in ranks:
            document = document_database.get(document_id)

            document['rank'] = ranks[document_id]

            documents.append(document)

        documents = sorted(documents, key=lambda d: d['rank'], reverse=True)

        return documents
