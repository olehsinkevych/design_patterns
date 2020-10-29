from abc import ABC, abstractmethod
from customization import Customization
from preparation import Preparation


class Product(ABC):
	@abstractmethod
	def make(self):
		pass


class Cappuccino(Product):
	def make(self, cust: Customization, prep: Preparation):
		print(f"Cappuccino{cust}, {prep}")
	def set_milk(self, prep):
		pass
	def set_sugar(self, prep):
		pass
	def set_coffee(self, prep):
		pass


class BlackCoffee(Product):
	def make(self, cust: Customization, prep: Preparation):
		print(f"BlackCoffee{cust}, {prep}")
	def set_water(self, prep):
		pass
	def set_coffee(self, prep):
		pass

class Lemonade(Product):
	def make(self, cust: Customization, prep: Preparation):
		print(f"Lemonade{cust}, {prep}")
	def set_water(self, prep):
		pass
	def set_sugar(self, prep):
		pass
	def ser_lemon_juice(self, prep):
		pass

class HotMilk(Product):
	def make(self, cust: Customization, prep: Preparation):
		print(f"HotMilk{cust}, {prep}")
	def set_milk(self, prep):
		pass


class CocaCola(Product):
	def make(self, cust: Customization, prep: Preparation):
		print(f"CocaCola{cust}, {prep}")
	def set_water(self, prep):
		pass
	def set_coke(self, prep):
		pass