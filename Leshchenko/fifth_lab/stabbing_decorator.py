from icharacter import ICharacter
from character_decorator import CharacterDecorator
import random


class StabbingDecorator(CharacterDecorator):
    def __init__(self, decorated_character):
        super(StabbingDecorator, self).__init__(decorated_character)

    def attack(self, victim: ICharacter):
        print(f"{self.get_name()} is stabbing {victim.get_name()}")
        amt = random.randint(0, 50)
        victim.dec_health(amt)
        super().attack(victim)
