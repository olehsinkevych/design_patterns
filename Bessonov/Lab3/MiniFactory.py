from Factory import *
from Parts import *
from Product import *


class CappuccinoFactory(CoffeeFactory):

    def make_preparation(self):
        return CappuccinoParts()
    def make_coffee(self):
        return CappuccinoCup()


class BlackCoffeeFactory(CoffeeFactory):

    def make_preparation(self):
        return BlackCoffeeParts()
    def make_coffee(self):
        return BlackCoffeeCup()

class HotMilkFactory(CoffeeFactory):

    def make_preparation(self):
        return HotMilkParts()
    def make_coffee(self):
        return HotMilkCup()