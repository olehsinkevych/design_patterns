class CarModel:
    def __init__(self, title = str):
        self.title = title


class Engine:
    def __init__ (self,capacity = float, numder_of_cylinders = int):
        self.capacity = capacity
        self.numder_of_cylinders = numder_of_cylinders
    def start(self):
        print('двигун запущений')
    def brake(self):
        print('двигун вимкнений')


class Body:
    def __init__ (self,number_of_doors = int):
        self.__number_of_doors = number_of_doors

    @property
    def number_of_doors(self):
        return self.__number_of_doors
    
    @number_of_doors.setter
    def number_of_doors(self, number_of_doors):
        if number_of_doors in range (1,5):
            self.__number_of_doors = number_of_doors
        else:
            print('недопустимий значення або дверей немає')


class Tire:
    def __init__ (self, width = float, air_pressure = float):
        self.width = width
        self.air_pressure = air_pressure


cla     ss Wheel:
    def __init__ (self,diameter = float):
        self.__diameter = diameter

    @property
    def diameter(self):
        return self.__diameter
    
    @diameter.setter
    def diameter(self, diameter):
        if diameter in range (1,100):
            self.__diameter = diameter
        else:
            print('недопустимий діаметр або колес немає')


class Brake:
    def __init__ (self, type = str):
        self.type = type


class Suspansion:
    def __init__(self, spring_rate = float):
        self.spring_rate = spring_rate


class GearBoxType:
    def __init__ (self,name = str,remarks = str):
        self.name = name
        self.remarks = remarks

class GearBox:
    def __init__(self, gear_ratio = float, current_gear = int):
        self.gear_ratio = gear_ratio
        self.current_gear = current_gear

    def shift_up(self):
        print('рухається вверх')

    def shift_down(self):
        print('рухається вниз')


class Car:
    def __init__(self,regiristration_num, year = int, license_number = str, capacity=Engine):
        self.regiristration_num = regiristration_num
        self.year = year
        self.license_number = license_number
        self.capacity = capacity

    def move_forward(self):
        print('прямує прямо')

    def move_backward(self):
        print('прямує назад')

    def stop(self):
        print('зупинилась')

    def tum_right(self):
        print('повернула направо')

    def tum_left(self):
        print('повернула наліво')
    def car1(self):
        print('реєстраційний номер \n', self.regiristration_num, 'рік авто\n', self.year, 'ліцензійний номер\n', self.license_number)

