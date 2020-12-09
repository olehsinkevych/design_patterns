from abc import abstractmethod, ABCMeta


class Product(metaclass=ABCMeta):
    @abstractmethod
    def product_name(self):
        pass

    @abstractmethod
    def build(self):
        pass
