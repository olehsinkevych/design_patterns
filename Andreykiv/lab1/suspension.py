from wheel import Wheel


class Suspension:
    """Docstring"""
    def __init__(self, springRate, wheel: Wheel):
        self.springRate = springRate
        self.wheel = wheel
