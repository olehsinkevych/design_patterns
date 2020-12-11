from abc import ABCMeta, abstractmethod


class ScreamBehavior(metaclass=ABCMeta):
    @abstractmethod
    def scream(self):
        pass