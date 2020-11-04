from abc import ABC,abstractmethod

class AbstractCoffee(ABC):

    @abstractmethod
    def assemble(self):
        pass

