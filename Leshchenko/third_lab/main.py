from abc import ABC, abstractmethod


class Customization:

    def __init__(self, extra_milk: float, sugar: float, mug_size: float):
        self.extra_milk = extra_milk
        self.sugar = sugar
        self.mug_size = mug_size


class Preparation:

    def __init__(self, milk: float, water: float, sugar: float, coke: float,
                 liquid_coffee: float, added_flavour: float, tea: float):
        self.milk = milk
        self.water = water
        self.sugar = sugar
        self.coke = coke
        self.liquid_coffee = liquid_coffee
        self.added_flavour = added_flavour
        self.tea = tea


class ProductFactory(ABC):

    @abstractmethod
    def get_product(self, customization):
        pass

    @staticmethod
    def get_product_factory(factory_type):
        pass


class CappuccinoFactory(ProductFactory):

    def get_product(self, cust: Customization):
        prep = Preparation(2.0, 1.0, 3.0, 3.0, 2.0, 0.0, 0.0)
        return Cappuccino(cust, prep)


class BlackCoffeeFactory(ProductFactory):

    def get_product(self, cust: Customization):
        prep = Preparation(0, 3, 2, 4, 3, 4, 0)
        return BlackCoffee(cust, prep)


class LemonadeFactory(ProductFactory):

    def get_product(self, cust: Customization):
        prep = Preparation(0, 5, 4, 0, 0, 4, 0)
        return Lemonade(cust, prep)


class HotMilkFactory(ProductFactory):

    def get_product(self, cust: Customization):
        prep = Preparation(5, 0, 3, 1, 1, 2, 0)
        return HotMilk(cust, prep)


class CocaColaFactory(ProductFactory):

    def get_product(self, cust: Customization):
        prep = Preparation(0, 3, 5, 0, 0, 4, 0)
        return CocaCola(cust, prep)


class Product(ABC):

    @abstractmethod
    def make(self):
        pass


class Cappuccino(Product):
    def __init__(self, cust: Customization, prep: Preparation):
        self.cust = cust
        self.prep = prep

    def make(self):
        print('The cappuccino is cooking')

    def set_coffee(self):
        self.prep.liquid_coffee()

    def set_sugar(self):
        self.prep.sugar()

    def set_milk(self):
        self.prep.milk()


class BlackCoffee(Product):

    def __init__(self, cust: Customization, prep: Preparation):
        self.cust = cust
        self.prep = prep

    def make(self):
        pass

    def set_water(self):
        self.prep.water()

    def set_coffee(self):
        self.prep.liquid_coffee()


class Lemonade(Product):

    def __init__(self, cust: Customization, prep: Preparation):
        self.cust = cust
        self.prep = prep

    def make(self):
        pass

    def set_water(self):
        self.prep.water()

    def set_sugar(self):
        self.prep.sugar()

    def set_lemon_juice(self):
        pass


class HotMilk(Product):

    def __init__(self, cust: Customization, prep: Preparation):
        self.cust = cust
        self.prep = prep

    def make(self):
        pass

    def set_milk(self):
        self.prep.milk()


class CocaCola(Product):

    def __init__(self, cust: Customization, prep: Preparation):
        self.cust = cust
        self.prep = prep

    def make(self):
        pass

    def set_water(self):
        self.prep.water()

    def set_coke(self):
        self.prep.coke()
