class GearBoxType:

    def __init__(self, name: str, remarks: str):
        self.name = name
        self.remarks = remarks


class GearBox:

    def __init__(self, gearRatio: float, currentGear: int,type:GearBoxType):
        self.gearRatio = gearRatio
        self.currentGear = currentGear
        self.type = type

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass


class Tire:

    def __init__(self, width: float, airPressure: float):
        self.width = width
        self.airPressure = airPressure



class Wheel:

    def __init__(self, diameter: float):
        self.diameter = diameter
        self.Tire = Tire



class Suspention:
    def __init__(self, springRate: float):
        self.springRate = springRate
        self.Wheel = Wheel
        self.Car = Car


class Brake:
    def __init__(self, type: str):
        self.type = type
        self.Wheel = Wheel
        self.Car = Car

    def apply(self):
        pass


class CarModel:
    def __init__(self, title: str):
        self.title = title

class Engine:

    def __init__(self, capacity: float, numberOfCylinders: int):
        self.capacity = capacity
        self.numberOfCylinders = numberOfCylinders
        self.engine =  Engine

    def start(self):
        pass

    def brake(self):
        pass

    def accerate(self):
        pass


class Body:
    def __init__(self, numberOfDoors: int):
        self.numberOfDoors = numberOfDoors
        self.car = Car

class Car:

    def __init__(self, registrationNum: str, year: int, licenseNum: str,gearBox:GearBox,suspension:Suspention,brake:Brake,body:Body,engine:Engine):
        self.registrationNum = registrationNum
        self.year = year
        self.licenseNum = licenseNum


    def moveForward(self):
        pass

    def moveBackward(self):
        pass

    def stop(self):
        pass

    def tumRight(self):
        pass

    def tumLeft(self):
        pass




# переробити, всі поля зробити нормальними
