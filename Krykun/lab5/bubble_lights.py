from tree_decorator import TreeDecorator
from christmas_treelmpl import ChristmasTree
from random import randint


class BubbleLights(TreeDecorator):
    def __init__(self, tree: ChristmasTree):
        self.tree = tree

    def decorate(self) -> str:
        lights = ['Red', 'Green', 'Blue']
        l = randint(0, 2)
        return f'{self.tree.decorate()} {lights[l]} Bubble Lights'
