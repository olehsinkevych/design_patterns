from abc import ABC, abstractmethod


class Burger(ABC):
    @abstractmethod
    def decorate(self) -> str:
        pass