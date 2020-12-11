from book import Book
from heavy_book import HeavyBook


class LightBook(Book):
    def __init__(self):
        self.available = False
        self.heavyBook = HeavyBook()
        self.heavy = False

    def get_name(self):
        if self.heavy:
            return self.heavyBook.get_name()
        else:
            return 'Light Name'

    def get_author(self):
        if self.heavy:
            return self.heavyBook.get_author()
        else:
            return 'Light Author'

    def is_available(self):
        return self.available

    def set_heavy(self):
        self.heavy = True