from icharacter import ICharacter


class CharacterDecorator(ICharacter):
    def __init__(self, decorated_character: ICharacter):
        self.decorated_character = decorated_character

    def get_health(self) -> int:
        return self.decorated_character.get_health()

    def dec_health(self, amt: int):
        self.decorated_character.dec_health(amt)

    def get_name(self) -> str:
        return self.decorated_character.get_name()

    def attack(self, victim: ICharacter):
        self.decorated_character.attack(victim)
