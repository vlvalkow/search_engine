class QueryProcessor:
    def __init__(self):
        self.terms = []

    def process(self, query):
        if query.startswith('"') and query.endswith('"'):
            self.terms = self.multi_word(query)
        else:
            self.terms = self.single_word(query)

        return self.terms

    def single_word(self, query):
        return query.split()

    def multi_word(self, query):
        return [query[1:-1]]
