from gearBox import GearBox
from engine import  Engine
from suspension import Suspension
from brake import  Brake
from body import Body


class Car(GearBox, Engine, Suspension, Brake, Body):
    def __init__(self, registration_num, year: int, license_number: str):
        self.registration_num = registration_num
        self.year = year
        self.license_number = license_number

    def move_forward(self):
        print('moveForward')

    def move_backward(self):
        print('moveBackward')

    def stop(self):
        print('stop')

    def turn_right(self):
        print('turnRight')

    def turn_left(self):
        print('turnLeft')

