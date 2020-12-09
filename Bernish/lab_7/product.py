from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def product_name(self):
        pass

    @abstractmethod
    def build(self):
        pass
