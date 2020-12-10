from abc import ABCMeta, abstractmethod
import datetime


class IBook(metaclass=ABCMeta):
    @abstractmethod
    def getName(self):
        """Name of the book"""
        pass

    @abstractmethod
    def getAuthor(self):
        """Author of the book"""
        pass

    @abstractmethod
    def isAvailable(self):
        """Do we have the book"""
        pass


class HeavyBook(IBook):
    def method(self):
        self.getName()
        self.getAuthor()
        self.isAvailable()

    def isAvailable(self):
        print("Yes")

    def getAuthor(self):
        print("Tolstoi")

    def getName(self):
        print("War and Peace")


class LightBook(IBook):
    def __init__(self):
        self.book = HeavyBook()

    def isAvailable(self):
        print("No")

    def getAuthor(self):
        print("Tolstoi")

    def getName(self):
        print("")

    def method(self, weight="light"):
        if weight == "light":
            self.getAuthor()
            self.isAvailable()
        else:
            self.book.method()
