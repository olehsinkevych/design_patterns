from abc import ABC, abstractmethod
from product import Cappuccino, BlackCoffee, Lemonade, HotMilk, CocaCola


class ProductFactory(ABC):
    """
    Abstract Factory
    """
    @abstractmethod
    def get_product(self):
        pass


class CappuccinoFactory(ProductFactory):
    """
    This class return class Cappuccino from product.py
    """
    def get_product(self):
        return Cappuccino


class BlackCoffeeFactory(ProductFactory):
    """
    This class return class BlackCoffee from product.py
    """
    def get_product(self):
        return BlackCoffee


class LemonadeFactory(ProductFactory):
    """
    This class return class Lemonade from product.py
    """
    def get_product(self):
        return Lemonade


class HotMilkFactory(ProductFactory):
    """
    This class return class HotMilk from product.py
    """
    def get_product(self):
        return HotMilk


class CocaColaFactory(ProductFactory):
    """
    This class return class CocaCola from product.py
    """
    def get_product(self):
        return CocaCola