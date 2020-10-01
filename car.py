from typing import List


class CarModel:
    def __init__(self, title: str):
        self.title = title

    def model(self):
        print("Model: " + self.title)


class Engine:
    def __init__(self, capacity: float, number_of_cylinders: int):
        self.__capacity = capacity
        self.__number_of_cylinders = number_of_cylinders

    @property
    def capacity(self):
        return self.__capacity

    @property
    def number_of_cylinders(self):
        return self.__number_of_cylinders

    @number_of_cylinders.setter
    def number_of_cylinders(self, number_of_cylinders):
        if number_of_cylinders in range(1, 8):
            self.__number_of_cylinders = number_of_cylinders
        else:
            print("\tnumberOfCylinders")

    def car_engine(self):
        print("Engine capacity: ", self.__capacity, "\nNumber of cylinders: ", self.__number_of_cylinders)

    def start(self):
        print("Engine start")

    def brake(self):
        print("Engine brake")

    def accelerate(self):
        print("Engine accelerate")


class Suspension:
    def __init__(self, spring_rate):
        self.__spring_rate = spring_rate

    @property
    def spring_rate(self):
        return self.__spring_rate

    @spring_rate.setter
    def spring_rate(self, spring_rate):
        if spring_rate is float:
            self.__spring_rate = spring_rate
        else:
            print("\tspring_rate")


class Body:
    def __init__(self, number_of_doors):
        self.__number_of_doors = number_of_doors

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, number_of_doors):
        if number_of_doors in range(0, 4):
            self.__number_of_doors = number_of_doors
        else:
            print("\tnumber_of_doors")


class Tire:
    def __init__(self, width, air_pressure):
        self.__width = width
        self.__air_pressure = air_pressure

    @property
    def width(self):
        return self.__width

    @property
    def air_pressure(self):
        return self.__air_pressure


class Wheel:
    def __init__(self, diameter, tire=Tire):
        self.__diameter = diameter
        self.tire = Tire

    @property
    def diameter(self):
        return self.__diameter


class Brake:
    def __init__(self, type):
        self.__type = type

    @property
    def type(self):
        return self.__type

    def apply(self, wheel: Wheel):
        print("\tbrake")


class Car:
    def __init__(self, registration_num: int, year: int, license_number: str, engine: Engine,
                 suspension: List, number_of_doors: Body, brake: Brake):
        self.__registration_num = registration_num
        self.__year = year
        self.__license_number = license_number
        self.engine = engine
        self.suspension = suspension
        self.number_of_doors = number_of_doors
        self.brake = brake

    @property
    def registration_num(self):
        return self.__registration_num

    @property
    def license_number(self):
        return self.__license_number

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        if year in range(0, 20):
            self.__year = year
        else:
            print("\tyear")

    def move_forward(self):
        print("\tDrive forward")

    def move_backward(self):
        print("\tDrive back")

    def stop(self):
        print("\tStop")

    def turn_right(self):
        print("\tDrive right")

    def turn_left(self):
        print("\tDrive left")

    def car_info(self):
        print("Registration number: ", self.__registration_num, "\nYear: ", self.__year, "\nLicense number: ",
              self.__license_number)


class GearBox:
    def __init__(self, gear_ratio: float, gear_box_type=None):
        self.__gear_ratio = gear_ratio
        self.__current_gear = 1
        self.gear_box_type = gear_box_type

    @property
    def gear_ratio(self):
        return self.__gear_ratio

    @gear_ratio.setter
    def gear_ratio(self, gear_ratio: float):
        if gear_ratio in range(1, 6):
            self.__current_gear = gear_ratio
            self.__gear_ratio = gear_ratio
        else:
            print("\tgearRatio")

    @property
    def current_gear(self):
        return self.__current_gear

    def car_gear(self):
        print("Gear: ", self.__current_gear)

    def shift_up(self):
        print("Gear up")
        self.__current_gear += 1

    def shift_down(self):
        print("Gear down")
        self.__current_gear -= 1


class GearBoxType:
    def __init__(self, name: str, remarks: str):
        self.name = name
        self.remarks = remarks