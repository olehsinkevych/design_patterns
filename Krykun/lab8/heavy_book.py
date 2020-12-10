from book import Book


class HeavyBook(Book):
    def __init__(self):
        self.available = False

    def get_name(self):
        return 'Heavy Name'

    def get_author(self):
        return 'Heavy Author'

    def is_available(self):
        return self.available
