from search_tool.search_engine.database import Document


class SearchEngine:
    def __init__(self, crawler, database_, indexer, filesystem):
        self.crawler = crawler
        self.database = database_
        self.indexer = indexer
        self.filesystem = filesystem
        self.inverted_index = {}

    def build_inverted_index(self):
        inverted_index = {}

        document = Document(self.database)

        self.crawler.crawl(document)

        for document in document.all():
            texts = self.crawler.parser.extract_visible_text(document)

            # TODO: Save to the filesystem in chunks to prevent running out of memory
            inverted_index = self.indexer.generate_index(document['id'], texts)

        self.filesystem.save('inverted_index.json', inverted_index)

        return inverted_index

    def load_inverted_index(self):
        self.inverted_index = self.filesystem.get('inverted_index.json')

    def get_inverted_index_for_term(self, term):
        inverted_index = []

        if term not in self.inverted_index:
            return inverted_index

        inverted_index = self.inverted_index[term]

        return inverted_index

    def find_documents(self, term):
        document = Document(self.database)

        inverted_index = self.get_inverted_index_for_term(term)

        documents = document.where_in('id', inverted_index)

        # for document in documents:
        #     document.update({
        #         'excerpt': self.crawler.parser.get_excerpt_for_term(document['content'], term)
        #     })

        return documents
