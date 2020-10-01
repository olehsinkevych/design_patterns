from Body import Body
from CarModel import CarModel
from Engine import Engine
from Suspencion import Suspension
from Brake import Brake
from GearBox import GearBox

class Car:
    def __init__(self, registration_num, year:int, license_number):
        self.registration_num=registration_num
        self.year=year
        self.license_number=license_number

    def move_forward(self):
        return self.move_forward
    def move_backward(self):
        return self.move_backward
    def stop(self):
        return self.stop
    def turn_right(self):
        return self.turn_right
    def turn_left(self):
        return self.turn_left

    def display_info_car(self):
        print("Registration number =",self.registration_num, " Year =",self.year, " Licence number",self.license_number )

my_car = Body(4)
my_car.display_info_body()
my_car = CarModel('Ferrari')
my_car.display_info_model()
my_car = Engine(3.2,8)
my_car.display_info_engine()
my_car = Suspension(66.7)
my_car.display_info_suspension()
my_car = Brake('handbrake')
my_car.display_info_brake()
my_car = GearBox(99.2,4)
my_car.display_info_gb()