from icharacter import ICharacter
from character_decorator import CharacterDecorator
import random


class CrushingDecorator(CharacterDecorator):
    def __init__(self, decorated_character):
        super(CrushingDecorator, self).__init__(decorated_character)

    def attack(self, victim: ICharacter):
        print(f"{self.get_name()} is crushing {victim.get_name()}")
        amt = random.randint(0, 40)
        victim.dec_health(amt)
        super().attack(victim)
