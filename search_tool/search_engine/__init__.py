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
        document_database = Document()
        terms = self.query_processor.process(query)

        matches = []
        for term in terms:
            if term not in self.inverted_index:
                return documents

            matches.append(set([appearance['document_id'] for appearance in self.inverted_index[term]]))

        document_ids = set.intersection(*matches)

        documents = document_database.where_in('id', document_ids)

        # for document in documents:
        #     document.update({
        #         'excerpt': self.crawler.parser.get_excerpt_for_term(document['content'], term)
        #     })

        return documents
