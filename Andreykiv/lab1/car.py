from engine import Engine
from gear_box import GearBox
from brake import Brake
from suspension import Suspension
from body import Body

class Car:
    """Docstring"""
    def __init__(self, registrationNum, year: int, licenseNumber: str, engine: Engine, gear_box: GearBox, brake: Brake,
                 suspension: Suspension, body: Body):
        self.registrationNum = registrationNum
        self.year = year
        self.licenseNumber = licenseNumber
        self.engine = engine
        self.gear_box = gear_box
        self.brake = brake
        self.suspension = suspension
        self.body = body


    def move_forward(self):
        # Program to print 'Car has moved forward'
        print('Car has moved forward')

    def moveBackward(self):
        # Program to print 'Car has moved backward'
        print('Car has moved backward')

    def stop(self):
        # Program to print 'Car has stopped'
        print('Car has stopped')

    def turn_right(self):
        # Program to print 'Car has turned right'
        print('Car has turned right')

    def turn_left(self):
        # Program to print 'Car has turned left'
        print('Car has turned left')

    def __str__(self):
        return 'This car has' + str(self.licenseNumber)
