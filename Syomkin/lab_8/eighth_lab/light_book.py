from book import Book
from heavy_book import HeavyBook


class LightBook(Book):
    def __init__(self) -> None:
        self._name = HeavyBook().get_name
        self._author = HeavyBook().get_author
        self._available = HeavyBook().is_available
        self._heavyBook = HeavyBook()

    @property
    def get_name(self):
        return self._name

    @property
    def get_author(self):
        return self._author

    @property
    def is_available(self):
        return self._available

    @is_available.setter
    def is_available(self, available):
        self._available = available

    def __str__(self):
        return f"Book name: {self._name} \n" \
               f"Book author: {self._author} \n" \
               f"Book available: {self._available} \n"

    def heavy_book(self):
        return self._heavyBook.__str__()
