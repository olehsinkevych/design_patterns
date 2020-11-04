from ABCProduct import *
from Parts import *

class CappuccinoCup(AbstractCoffee):
    def assemble(self, parts):
        print(f"Cappuccino is made here using {parts}")

class BlackCoffeeCup(AbstractCoffee):
    def assemble(self, parts):
        print(f"BlackCoffee is made here using {parts}")

class HotMilkCup(AbstractCoffee):
    def assemble(self, parts):
        print(f"HotMilk is made here using {parts}")



