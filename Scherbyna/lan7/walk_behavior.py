from abc import ABCMeta, abstractmethod


class WalkBehavior(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass