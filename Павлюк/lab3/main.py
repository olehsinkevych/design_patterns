from abc import ABCMeta, abstractmethod
from typing import List


class Item(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass


class BigMac(Item):
    configs = {'Small': 1, 'Medium': 2, 'Big': 3, 'Giant': 3.5}

    def init(self, size: str):
        self.size = size
        self.price = BigMac.configs[size]

    def get_name(self) -> str:
        return f'Big Mac size of {self.size}'

    def get_price(self) -> float:
        return self.price


class IceCream(Item):
    configs = {'KitKat': 5, 'Chocolate': 3, 'Vanilla': 2}

    def init(self, kind: str):
        self.kind = kind
        self.price = IceCream.configs[kind]

    def get_name(self) -> str:
        return f'Ice Cream kind of {self.kind}'

    def get_price(self) -> float:
        return self.price


class Tea(Item):
    configs = {'Small': 1, 'Medium': 2, 'Big': 3}

    def init(self, size: str):
        self.size = size
        self.price = Tea.configs[size]

    def get_name(self) -> str:
        return f'Tea size of {self.size}'

    def get_price(self) -> float:
        return self.price


class CocaCola(Item):
    configs = {'Small': 2, 'Medium': 3, 'Big': 5}

    def init(self, size: str):
        self.size = size
        self.price = CocaCola.configs[size]

    def get_name(self) -> str:
        return f'Coca Cola size of {self.size}'

    def get_price(self) -> float:
        return self.price


class Meal:
    def init(self, items: List[Item]):
        self.items = items

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, item: List[Item]):
        self._items = item

    def get_cost(self):
        total_price = 0
        for item in self.items:
            total_price += item.get_price()
            return total_price

    def str(self):
        pass


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def create_menu_1(self):
        pass

    @abstractmethod
    def create_menu_2(self):
        pass


class MealBuilder(Builder):
    def create_menu_1(self) -> Meal:
        big_mac = BigMac('Big')
        ice_cream = IceCream('KitKat')
        coca_cola = CocaCola("Medium")
        meal = Meal(items=[big_mac, ice_cream, coca_cola])
        return meal

    def create_menu_2(self) -> Meal:
        big_mac = BigMac('Small')
        ice_cream = IceCream('Vanilla')
        meal = Meal(items=[big_mac, ice_cream])
        return meal

    def sell_tea(self) -> Meal:
        tea = Tea()
        meal = Meal(items=[tea])
        return meal


new_meal_builder = MealBuilder()
meal = new_meal_builder.create_menu_1()
print(meal.get_cost())