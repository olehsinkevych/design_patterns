from tire import Tire


class Wheel():
    def __init__(self, diameter, tire: Tire):
        self.diameter = diameter
        self.tire = tire
