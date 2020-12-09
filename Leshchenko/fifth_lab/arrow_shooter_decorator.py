from icharacter import ICharacter
from character_decorator import CharacterDecorator
import random


class ArrowShouterDecorator(CharacterDecorator):
    def __init__(self, decorated_character):
        super(ArrowShouterDecorator, self).__init__(decorated_character)

    def attack(self, victim: ICharacter):
        print(f"{self.get_name()} is shooting an arrow at {victim.get_name()}")
        amt = random.randint(0, 30)
        victim.dec_health(amt)
        super().attack(victim)
