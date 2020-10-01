"""Description"""
from typing import List


class Suspension:
    """Docstring"""

    def __init__(self, spring_rate):
        self.spring_rate = spring_rate

    @property
    def spring_rate(self):
        return self._spring_rate

    @spring_rate.setter
    def spring_rate(self, value):
        if isinstance(value, int) and value > 0:
            self._spring_rate = value


class CarModel:
    def __init__(self, title: str):
        self.title = title


class Body:
    """Docstring"""

    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    @property
    def number_of_doors(self):
        return self._number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        if isinstance(value, int) and value > 0:
            self._number_of_doors = value


class Engine:
    """Docstring"""

    def __init__(self, capacity, num_cylinders):
        self.capacity = capacity
        self.num_cylinders = num_cylinders

    def start(self):
        '''Coments'''
        print('Engine has been started')


class GearBox:
    def __init__(self, gear_ratio: float, currentGear:int, gearboxtype):
        self.gear_ratio = gear_ratio
        self.currentGear = currentGear
        self.gearboxtype = gearboxtype

    def shiftUp(self):
        self.currentGear = self.currentGear + self.gear_ratio
        print("Current Gear is ", self.currentGear)

    def shiftDown(self):
        self.currentGear = self.currentGear - self.gear_ratio
        if self.currentGear < -1:
            print("There are no lower gear")
        else:
            print("Current Gear is ", self.currentGear)


class GearBoxType:
    def __init__(self, name: str, remarks: str):
        self.name = name
        self.remarks = remarks


class Suspension:
    def __init__(self, springRate: float, wheel):
        self.springRate = springRate
        self.wheel = wheel


class Brake:
    def __init__(self, type: str, wheel):
        self.type = type
        self.wheel = wheel

    def apply(self):
        print("Applied")


class Wheel:
    def __init__(self, diameter: float, tire):
        self.diameter = diameter
        self.tire = tire


class Tire:
    def __init__(self, width: float, air_preassure: float):
        self.width = width
        self.air_pressure = air_preassure


class Car:
    """Docstring"""
    def __init__(self, engine: Engine, suspension: List, body: Body, brake: Brake,
                 registration_num=0, year=0, license_number=''):
        self.registration_num = registration_num
        self.year = year
        self.license_number = license_number
        self.engine = engine
        self.body = body
        self.suspension = suspension
        self.brake = brake

    @property
    def registration_num(self):
        return self._registration_num

    @registration_num.setter
    def registration_num(self, value):
        if isinstance(value, int) and value > 0:
            self._registration_num = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and value > 0:
            self._year = value

    @property
    def license_number(self):
        return self._license_number

    @license_number.setter
    def license_number(self, value):
        if isinstance(value, str) and len(value) > 1:
            self._license_number = value

    def move_forward(self):
        """Docstring"""
        print('Car has moved forward')

    def move_backward(self):
        """Docstring"""
        print('Car has moved back forward')

    def stop(self):
        """Docstring"""
        print('Car has stoped')

    def turn_right(self):
            print("turning right")

    def turn_left(self):
            print("turning left")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
