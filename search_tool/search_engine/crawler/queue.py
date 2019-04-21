class Queue:
    def __init__(self):
        self.list = []

    def all(self):
        return self.list

    def is_empty(self):
        return len(self.list) == 0

    def next(self):
        iterator = iter(self.list)
        return next(iterator)

    def add(self, url):
        self.list.append(url)

    def remove(self, url):
        self.list.remove(url)

    def empty(self):
        self.list = []
