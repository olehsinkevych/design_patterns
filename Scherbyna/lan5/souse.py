from burger_decorator import Burger_Decorator
from ingridient import Burger
from random import randint


class Souse(Burger_Decorator):
    def __init__(self, bread: Burger):
        self.bread = bread

    def decorate(self) -> str:
        souse = ['ketchup','mustard','mayonnaise']
        s = randint(0, 2)
        return f'{self.bread.decorate()} {souse[s]} Souse'