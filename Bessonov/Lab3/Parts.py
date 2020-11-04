from MiniFactory import *
from PartsABC import *

class CappuccinoParts(CoffeeParts):
    def build(self):
        print("Cappuccino parts are made")

class BlackCoffeeParts(CoffeeParts):
    def build(self):
        print("BlackCoffee parts are made")

class HotMilkParts(CoffeeParts):
    def build(self):
        print("Hotmilk parts are made")

        