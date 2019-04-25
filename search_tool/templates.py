class BuildTemplate:
    def render(self):
        return 'The inverted index was built successfully.'


class LoadTemplate:
    def render(self):
        return 'The inverted index was loaded successfully.'


class PrintTemplate:
    def render(self, inverted_index):
        return str(inverted_index)


class FindTemplate:
    def render(self, documents, term):
        response = \
            '==================================================\n' \
            ' Found ' + str(len(documents)) + ' results for query ' + term + ': \n' \
            '==================================================\n' \
            '\n'

        for document in documents:
            response += '--------------------------------------------------\n'
            response += ' ' + document['title'] + '\n'
            response += ' ' + document['url'] + '\n'
            response += '--------------------------------------------------\n'
            response += '\n'

        return response


class HelpTemplate:
    def render(self):
        return \
            '==================================================\n' \
            ' List of available commands \n' \
            '==================================================\n' \
            ' build - crawls the website and builds an inverted index\n' \
            ' load  - loads the inverted index from the filesystem\n' \
            ' print - prints the inverted index for an entered term\n' \
            ' find  - finds web pages containing an entered term\n' \
            ' help  - lists all available application commands\n' \
            ' exit  - closes the application\n' \
            '--------------------------------------------------\n'


class NotFoundTemplate:
    def render(self, action):
        return 'ERROR: Action ' + action + ' does not exist.'
