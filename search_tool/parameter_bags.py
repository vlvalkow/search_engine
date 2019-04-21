class ParameterBag:
    def print(self):
        return {
            'term': input('Enter term: '),
        }

    def find(self):
        return {
            'term': input('Enter term: '),
        }


class TestParameterBag:
    def print(self):
        return {
            'term': 'apple',
        }

    def find(self):
        return {
            'term': 'cat',
        }
