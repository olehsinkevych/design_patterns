from christmas_treelmpl import ChristmasTreelmpl
from tree_topper import TreeTopper
from tinsel import Tinsel
from garland import Garland
from bubble_lights import BubbleLights


christmas = ChristmasTreelmpl()
tree1 = TreeTopper(christmas)
tree2 = Tinsel(christmas)
tree3 = Garland(christmas)
tree4 = BubbleLights(christmas)
print(f'{tree1.decorate()}, \n{tree2.decorate()}, \n{tree3.decorate()}, \n{tree4.decorate()}')
