from abc import abstractmethod, ABCMeta


class ICharacter(metaclass=ABCMeta):
    @abstractmethod
    def get_health(self) -> int:
        pass

    @abstractmethod
    def dec_health(self, amt: int):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def attack(self, victim):
        pass
