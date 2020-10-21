from wheel import Wheel


class Brake(Wheel):
    def __init__(self, type: str):
        self.type = type

    def apply(self):
        print('apply')