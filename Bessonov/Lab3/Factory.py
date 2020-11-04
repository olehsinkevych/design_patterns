from abc import ABC, abstractmethod


class CoffeeFactory(ABC):

    @abstractmethod
    def make_preparation(self):
        pass
    @abstractmethod
    def make_coffee(self):
        pass
