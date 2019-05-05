import re


class Indexer:
    def __init__(self):
        self.index = {}

    def generate_index(self, document_id, texts):
        terms = []

        for text in texts:
            terms.extend(self.generate_ngrams(text, 1))
            terms.extend(self.generate_ngrams(text, 2))
            terms.extend(self.generate_ngrams(text, 3))

            for term in terms:
                if term in self.index:
                    self.update_existing_term(term, document_id)
                else:
                    self.add_new_term(term, document_id)

            # Reset the list so it does not contain terms from previous texts
            terms = []

        return self.index

    def update_existing_term(self, term, document_id):
        appearance = next((appearance for appearance in self.index[term] if appearance["document_id"] == document_id),
                          None)

        if appearance:
            appearance['frequency'] += 1
        else:
            self.index[term].append(Appearance(document_id, 1).__dict__)

    def add_new_term(self, term, document_id):
        self.index[term] = [Appearance(document_id, 1).__dict__]

    def generate_ngrams(self, s, n):
        # Replace all none alphanumeric characters with spaces
        s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)

        # Break sentence in the token, remove empty tokens
        tokens = [token for token in s.split(" ") if token != ""]

        # Use the zip function to help us generate n-grams
        # Concatenate the tokens into ngrams and return
        ngrams = zip(*[tokens[i:] for i in range(n)])
        return [" ".join(ngram) for ngram in ngrams]


class Appearance:
    def __init__(self, document_id, frequency):
        self.document_id = document_id
        self.frequency = frequency
