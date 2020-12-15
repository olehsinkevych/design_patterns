from abc import ABC, abstractmethod
from customization import Customization
from preparation import Preparation


class Product(ABC):
    @abstractmethod
    def make(self):
        pass


class Cappuccino(Product):
    def make(self, cust: Customization, prep: Preparation):
        print(f"CAPPUCCINO {cust}, {prep}")

    @staticmethod
    def set_milk():
        print("MILK SET")

    @staticmethod
    def set_sugar():
        print("SUGAR SET")

    @staticmethod
    def set_coffee():
        print("COFFEE SET")


class BlackCoffee(Product):
    def make(self, cust: Customization, prep: Preparation):
        print(f"BLACK COFFEE {cust}, {prep}")

    @staticmethod
    def set_water():
        print("WATER SET")

    @staticmethod
    def set_coffee():
        print("COFFEE SET")


class Lemonade(Product):
    def make(self, cust: Customization, prep: Preparation):
        print(f"LEMONADE {cust}, {prep}")

    @staticmethod
    def set_water():
        print("WATER SET")

    @staticmethod
    def set_sugar():
        print("SUGAR SET")

    @staticmethod
    def set_lemon_juice():
        print("LEMON JUICE SET")


class HotMilk(Product):
    def make(self, cust: Customization, prep: Preparation):
        print(f"HOT MILK {cust}, {prep}")

    @staticmethod
    def set_milk(cust):
        print(f"MILK SET, EXTRA MILK {cust}")


class CocaCola(Product):
    def make(self, cust: Customization, prep: Preparation):
        print(f"COCA COLA {cust}, {prep}")

    @staticmethod
    def set_water():
        print("WATER SET")

    @staticmethod
    def set_coke():
        print("COKE SET")