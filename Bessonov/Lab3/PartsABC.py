from abc import ABC,abstractmethod

class CoffeeParts(ABC):
    @abstractmethod
    def build(self):
        pass
