from tree_decorator import TreeDecorator
from christmas_treelmpl import ChristmasTree


class TreeTopper(TreeDecorator):
    def __init__(self, tree: ChristmasTree):
        self.tree = tree

    def decorate(self) -> str:
        return f'{self.tree.decorate()}Topper'
