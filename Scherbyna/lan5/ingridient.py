from burger import Burger


class Ingridient(Burger):
    def decorate(self) -> str:
        return 'Decorate with '