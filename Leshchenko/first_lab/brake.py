from wheel import Wheel


class Brake():
    def __init__(self, type, wheel: Wheel):
        self.type = type
        self.wheel = wheel

    def apply(self):
        print("apply")
