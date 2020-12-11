from raccoon import Raccoon
from scream import Scream
from no_walk import NoWalk


class ModelRaccoon(Raccoon):
    def __init__(self):
        self.walk_behavior = NoWalk()
        self.scream_behavior = Scream()

    def display(self):
        print("Модель єнота")