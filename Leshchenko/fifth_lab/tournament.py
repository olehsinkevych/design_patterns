from character_decorator import CharacterDecorator


class Tournament:
    def start(self, a: CharacterDecorator, b: CharacterDecorator):
        while a.get_health() and b.get_health():
            a.attack(b)
            b.attack(a)
            if not a.get_health():
                print(f"Winner {b.get_name()}")
                return b
            elif not b.get_health():
                print(f"Winner {a.get_name()}")
                return a
