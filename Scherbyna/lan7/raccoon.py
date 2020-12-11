from abc import ABCMeta
from scream_behavior import ScramBehavior
from walk_behavior import WalkBehavior
from wash_dishes_behavior import WashDishesBehavior


class Raccoon(metaclass=ABCMeta):
    walk_behavior: WalkBehavior
    scream_behavior: ScramBehavior
    wash_dishes_behavior: WashDishesBehavior

    def display(self):
        pass

    def perform_walk(self):
        self.walk_behavior.walk()

    def walks(self):
        print("Всі єноти ходять")

    def perform_scream(self):
        self.scream_behavior.scream()

    def perform_wash_dishes(self):
        self.wash_dishes_behavior.wash()

    def set_walk_behavior(self, walkbeh: WalkBehavior):
        self.walk_behavior = walkbeh

    def set_scream_behavior(self, screambeh: ScramBehavior):
        self.scream_behavior = screambeh

    def set_wash_dishes_behavior(self, washbeh: WashDishesBehavior):
        self.wash_dishes_behavior = washbeh