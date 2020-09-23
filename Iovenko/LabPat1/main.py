class CarModel:
    def __init__(self, title: str):
        self.title = title


class Engine:
    def __init__(self, capacity: float, numberOfCylinders: int):
        self.capacity = capacity
        self.numberOfCylinders = numberOfCylinders

    def start(self):
        pass

    def brake(self):
        pass

    def accerate(self):
        pass


class Body:
    def __init__(self, numberOfDoors: int):
        self.numberOfDoors = numberOfDoors


class Tire:
    def __init__(self, width: float, airPressure: float):
        self.width = width
        self.airPressure = airPressure


class Wheel:
    def __init__(self, diameter: float, tire: Tire):
        self.diameter = diameter

        self.__tire = tire


class Brake:
    def __init__(self, type: str, wheel: Wheel):
        self.type = type

        self.__wheel = wheel

    def apply(self):
        pass


class Suspension:
    def __init__(self, springRate: float, wheel: Wheel):
        self.springRate = springRate

        self.__wheel = wheel


class GearBoxType:
    def __init__(self, name: str, remarks: str):
        self.name = name
        self.remarks = remarks


class GearBox:
    def __init__(self, gearRatio: float, currentGear: int, gear_box_type: GearBoxType):
        self.gearRatio = gearRatio
        self.currentGear = currentGear

        self.__gear_box_type = gear_box_type

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass


class Car:

    def __init__(self, registrationNum, year: int, licenseNumber: str, gear_box: GearBox, car_model: CarModel,
                 engine: Engine, body: Body, suspension: Suspension, brake: Brake):
        self.registrationNum = registrationNum
        self.year = year
        self.licenseNumber = licenseNumber

        self.__gear_box = gear_box
        self.__car_model = car_model
        self.__engine = engine
        self.__body = body
        self.__suspension = suspension
        self.__brake = brake

    def moveForward(self):
        pass

    def moveBackward(self):
        pass

    def stop(self):
        pass

    def turnRight(self):
        pass

    def turnLeft(self):
        pass
