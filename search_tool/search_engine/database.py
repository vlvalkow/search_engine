from search_tool.search_engine.filesystem import Filesystem


class Model:
    def __init__(self):
        self.filesystem = Filesystem()
        self.entries = []

        data = self.filesystem.get('database.json')

        if data:
            self.entries = data

    def get(self, id_):
        for entry in self.entries:
            if entry['id'] == id_:
                return entry

    def where_in(self, key, haystack):
        entries = []

        for entry in self.entries:
            for appearance in haystack:
                if entry[key] == appearance['document_id']:
                    entries.append(entry)

        return entries

    def save(self, entry):
        entry['id'] = len(self.entries) + 1
        self.entries.append(entry)

    def all(self):
        return self.entries


class Document(Model):
    def __init__(self):
        Model.__init__(self)
