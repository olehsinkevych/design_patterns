from Tire import Tire

class Wheel:
    def __init__(self,diameter:float):
        self.diameter=diameter

    def display_info_wheel(self):
        print("Diameter of wheel =",self.diameter)

    my_car=Tire(1.90,22.4)
    my_car.display_info_tire()

