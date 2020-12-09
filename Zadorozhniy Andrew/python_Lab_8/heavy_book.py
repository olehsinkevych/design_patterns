from book import Book


class HeavyBook(Book):

    def __init__(self) -> None:
        self._name = "The Da Vinci Code"
        self._author = "Dan Brown"
        self._description = "is a novel by English writer Daniel Gerhard Brown, " \
                            "The Da Vinci Code, became a bestseller, going to the top of the New York Times Best Seller"\
                            "its first week of release in 2003"
        self._rating = "6,6/10"
        self._available = True

    @property
    def get_name(self):
        return self._name

    @property
    def get_author(self):
        return self._author

    @property
    def get_description(self):
        return self._description

    @property
    def get_rating(self):
        return self._rating

    @property
    def is_available(self):
        return self._available

    @is_available.setter
    def is_available(self, available):
        self._available = available

    def __str__(self):
        return f"Book name: {self._name} \n" \
               f"Book author: {self._author} \n" \
               f"Book description: {self._description} \n" \
               f"Book rating: {self._rating} \n" \
               f"Book available: {self._available} \n"