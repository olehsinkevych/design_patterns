from wheel import Wheel


class Suspension():
    def __init__(self, springRate, wheel: Wheel):
        self.springRate = springRate
        self.wheel = wheel
