from .templates import *


class Controller:
    def build(self, search_engine):
        search_engine.build_inverted_index()

        return BuildTemplate().render()

    def load(self, search_engine):
        search_engine.load_inverted_index()

        return LoadTemplate().render()

    def print(self, search_engine, term):
        inverted_index = search_engine.get_inverted_index_for_term(term)

        return PrintTemplate().render(inverted_index)

    def find(self, search_engine, term):
        documents = search_engine.find_documents(term)

        return FindTemplate().render(documents, term)

    def help(self):
        return HelpTemplate().render()

    def not_found(self, action):
        return NotFoundTemplate().render(action)
