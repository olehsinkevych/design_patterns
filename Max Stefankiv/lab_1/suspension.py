from wheel import  Wheel


class Suspension(Wheel):
    def __init__(self, springRate: float):
        self.springRate = springRate