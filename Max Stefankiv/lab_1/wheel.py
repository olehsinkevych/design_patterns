from tire import Tire


class Wheel(Tire):
    def __init__(self, diameter: float):
        self.diameter = diameter