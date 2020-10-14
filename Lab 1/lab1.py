from typing import List
from engine import Engine
from GearBox import GearBox
from GearBoxType import GearBoxType
from Suspension import Suspension
from Body import Body
from Tire import Tire
from Wheel import Wheel
from Brake import Brake
from CarModel import CarModel


class Car:
    def __init__(self,engine: Engine, gear_box: GearBox, gear_box_type: GearBoxType, suspension: Suspension,
                 body: Body, tire: Tire, wheel: Wheel, brake: Brake,registration_num: int, year: int,
                 license_number: str, car_model: CarModel):
        self._registration_num = registration_num;
        self._year = year;
        self._license_number = license_number;
        self.engine = engine
        self.gear_box = gear_box
        self.gear_box_type = gear_box_type
        self.suspension = suspension
        self.body = body
        self.tire = tire
        self.wheel = wheel
        self.brake = brake
        self.car_model = car_model


        @property
        def registration_num(self,value):
            return self._registration_num

        @registration_num.setter
        def registration_num(self,value):
            if isinstance(value,int) and value > 0:
                self._registration_num = value

        @property
        def year(self):
            return self._year

        @year.setter
        def year(self,value):
            if isinstance(value,int) and value > 0:
                self._year = value

        @property
        def license_number(self):
            return self._license_number

        @license_number.setter
        def year(self,value):
            if isinstance(value,int) and value > 0:
                self._year = value

    def move_forward(self):
        print('Car has moved backward')

    def move_backward(self):

        print('Car has moved backward')
    def stop(self):
        print('Car has stopped')

    def turn_right(self):
        print('Car has turned right')

    def turn_left(self):
        print('Car has turned left')

    def __str__(self):
        return 'Test'








