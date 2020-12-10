from abc import ABC, abstractmethod
from random import randint


class ChristmasTree(ABC):
    @abstractmethod
    def decorate(self) -> str:
        pass
