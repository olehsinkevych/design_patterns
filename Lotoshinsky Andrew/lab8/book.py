from abc import ABCMeta, abstractmethod


class Book(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_author(self):
        pass

    @abstractmethod
    def is_available(self):
        pass

    @abstractmethod
    def __str__(self):
        pass