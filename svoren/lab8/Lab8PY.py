import abc

class Book(abc.ABC):
    @abc.abstractmethod
    def getName(self):
        pass
    @abc.abstractmethod
    def getAuthor(self):
        pass
    @abc.abstractmethod
    def Include(self):
        pass

class HeavyBook(Book):
    def __init__(self):
        self.include = False
    def getName(self):
        return "Війна і Мир"
    def getAuthor(self):
        return "Лев Товстий"
    def Include(self):
        return  self.include

class LightBook(Book):
    def __init__(self):
        self.include = False
        self.heavyBook = HeavyBook()
        self.heavy = False
    def getName(self):
        if self.heavy:
            return self.heavyBook.getName()
        return "Першому гравцю приготуватись"
    def getAuthor(self):
        if self.heavy:
            return self.heavyBook.getAuthor()
        return "Ернест Клайн"
    def Include(self):
        return  self.include
    def useHeavy(self):
        self.heavy = True

book = LightBook()
print(book.getAuthor())
print(book.getName())
book.useHeavy()
print(book.getAuthor())
print(book.getName())