class SearchTool:
    def __init__(self, router, search_engine_):
        self.running = True
        self.first_run = True
        self.router = router
        self.search_engine = search_engine_

    def run(self):
        while self.running:
            if self.first_run:
                self.handle_first_run()

            action = input('Enter an action: ')

            if action == 'exit':
                self.running = False
                print('Goodbye!')
                continue

            response = self.router.route(action, self.search_engine)
            print(response)

    def handle_first_run(self):
        print('\n')
        print('=' * 50)
        print(' Welcome!')
        print('=' * 50)
        print(' For list of available actions type "help"')
        print('-' * 50)
        print('\n')
        self.first_run = False
