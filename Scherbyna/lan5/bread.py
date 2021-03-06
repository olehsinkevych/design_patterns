from burger_decorator import Burger_Decorator
from ingridient import Burger

class Bread(Burger_Decorator):
    def __init__(self, bread: Burger):
        self.bread = bread

    def decorate(self) -> str:
        return f'{self.bread.decorate()}Bread'