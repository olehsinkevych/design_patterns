from Wheel import Wheel

class Suspension:
    def __init__(self,spr_rate:float):
        self.spr_rate=spr_rate

    def display_info_suspension(self):
        print("Suspension =",self.spr_rate)

my_car=Wheel(1.85)
my_car.display_info_wheel()
