from abc import ABC, abstractmethod

class ChristmasTree(ABC):
    @abstractmethod
    def decorate(self) -> str
        pass

class ChristmasTreelmpl(ChristmasTree):
    def __init__(self,christmas_tree_lmpl):
        self.christmas_tree_lmpl=christmas_tree_lmpl

    def decorate(self) -> str:
        return self.christmas_tree_lmpl


class TreeDecorator(ChristmasTree):
    def __init__(self,decorator_tree):
        self.decorator_tree=decorator_tree

    @property
    def tree(self):
        return self.decorator_tree

    @tree.setter
    def tree(self, value):
        self.decorator_tree = value

class TreeTopper(TreeDecorator):
    def __init__(self,decorator_tree,n:str):
        super.__init__(decorator_tree)
        self.n=n

    def decorate(self) -> str:
        return self.decorator_tree

    def decorate_tree_topper(self) -> str:
        return self.n.decorate_tree_topper()


class Tinsel(TreeDecorator):
    def __init__(self,decorator_tree,n:str):
        super.__init__(decorator_tree)
        self.n=n

    def decorate(self) -> str:
        return self.decorator_tree

    def decorate_tinsel(self) -> str:
        return self.n.decorate_tinsel()


class Garland(TreeDecorator):
    def __init__(self,decorator_tree,n:str):
        super.__init__(decorator_tree)
        self.n=n

    def decorate(self) -> str:
        return self.decorator_tree

    def decorate_garland(self) -> str:
        return self.n.decorate_garland()


class BubbleLight(TreeDecorator):
    def __init__(self,decorator_tree,n:str):
        super.__init__(decorator_tree)
        self.n=n

    def decorate(self) -> str:
        return self.decorator_tree

    def decorate_garland(self) -> str:
        return self.n.decorate_garland()


from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> int:
        pass


class ItalianPizza(Pizza):
    def __init__(self, italian_pizza):
        self.italian_pizza = italian_pizza

    def get_name(self) -> str:
        return self.italian_pizza

    def get_cost(self):
        return 10


class BulgarianPizza(Pizza):
    def __init__(self, bulgarian_pizza):
        self.bulgarian_pizza = bulgarian_pizza

    def get_name(self) -> str:
        return self.bulgarian_pizza

    def get_cost(self) -> int:
        return 8


class PizzaDecorator(Pizza):
    def __init__(self, decorator_pizza):
        self.decorator_pizza = decorator_pizza

    @property
    def pizza(self):
        return self.decorator_pizza

    @pizza.setter
    def pizza(self, value):
        self.decorator_pizza = value


class TomatoPizza(PizzaDecorator):
    def __init__(self, decorator_pizza, n: str):
        super().__init__(decorator_pizza)
        self.n = n

    def get_name(self) -> str:
        return self.n.get_name()

    def get_cost(self) -> int:
        return self.decorator_pizza.get_cost() + 3


class CheesePizza(PizzaDecorator):
    def __init__(self, decorator_pizza, n: str):
        super().__init__(decorator_pizza)
        self.n = n

    def get_name(self) -> str:
        return self.n.get_name()

    def get_cost(self) -> int:
        return self.decorator_pizza.get_cost() + 2


pizza_italiano = ItalianPizza("Italian")
pizza_bulgariano = BulgarianPizza("Bulgarian")
pizza1 = TomatoPizza(pizza_italiano, "Tomato Pizza")
pizza2 = TomatoPizza(pizza_bulgariano, "Pizza Tomato")
pizza3 = CheesePizza(pizza1, "Tomato + Cheese")

print(f"{pizza_italiano.get_name()}, {pizza1.n}, {pizza1.get_cost()}, {pizza3.n}, {pizza2.get_cost()}")
print(f"{pizza1.get_cost()}, {pizza1.n}, {pizza2.get_cost()}, {pizza_italiano.get_name()}, {pizza_italiano.get_cost()}")