from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_author(self):
        pass

    @abstractmethod
    def is_available(self):
        pass