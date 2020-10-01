from Wheel import Wheel

class Brake:
    def __init__(self,type):
        self.type= type
    def apply(self):
        return self.apply

    def display_info_brake(self):
        print("Brake is",self.type)

my_car=Wheel(1.75)
my_car.display_info_wheel()
