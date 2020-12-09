from icharacter import ICharacter
import random


class Character(ICharacter):
    def __init__(self, name: str, health: int = 100):
        self._name = name
        self._health = health

    def get_health(self) -> int:
        return self._health

    def dec_health(self, amt: int):
        self._health = max(0, self._health - amt)

    def get_name(self) -> str:
        return self._name

    def attack(self, victim: ICharacter):
        if self._health > 0 and victim.get_health() > 0:
            print(f"{self.get_name()} is attacking {victim.get_name()}")
            amt = random.randint(0, 100)
            victim.dec_health(amt)
