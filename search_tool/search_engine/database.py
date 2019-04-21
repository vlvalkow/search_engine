class Database:
    def __init__(self):
        self.entries = []


class Model:
    def __init__(self, database):
        self.database = database

    def get(self, id_):
        for entry in self.database.entries:
            if entry['id'] == id_:
                return entry

    def where_in(self, key, haystack):
        entries = []

        for entry in self.database.entries:
            for appearance in haystack:
                if entry[key] == appearance['document_id']:
                    entries.append(entry)

        return entries

    def save(self, entry):
        entry['id'] = len(self.database.entries) + 1
        self.database.entries.append(entry)

    def all(self):
        return self.database.entries


class Document(Model):
    def __init__(self, database):
        Model.__init__(self, database)
