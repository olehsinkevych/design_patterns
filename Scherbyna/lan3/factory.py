from abc import ABC, abctractmetothod
from product import Cappuccino, BlackCoffee, Lemonade, HotMilk, CocaCola

class ProductFactory(ABC):
	@abctractmetothod
	def get_product(self):
		pass


class CappuccinoFactory(ProductFactory):
	def get_product(self):
		return Cappuccino


class BlackCoffeFactory(ProductFactory):
	def get_product(self):
		return BlackCoffee


class LemonadeFactory(ProductFactory):
	def get_product(self):
		return Lemonade


class HotMilkFactory(ProductFactory):
	def get_product(self):
		return HotMilk

		
class CocaColaFactory(ProductFactory):
	def get_product(self):
		return CocaCola