class GearBoxType:
    def __init__(self, name, remarks):
        self.name = name
        self.remarks = remarks


class GearBox(GearBoxType):
    def __init__(self, gearRatio, currentGear):
        self.gearRatio = gearRatio
        self.currentGear = currentGear

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass


class Engine:
    def __init__(self, capacity, numberOfCylinders):
        self.capacity = capacity
        self.numberOfCylinders = numberOfCylinders

    def start(self):
        pass

    def brake(self):
        pass

    def accerate(self):
        pass


class Body:
    def __init__(self, numberOfDoors):
        self.numberOfDoors = numberOfDoors


class Tire:
    def __init__(self, width, airPressure):
        self.width = width
        self.airPressure = airPressure


class Wheel(Tire):
    def __init__(self, diameter):
        self.diameter = diameter


class Suspension(Wheel):
    def __init__(self, springRate):
        self.springRate = springRate


class Brake(Wheel):
    def __init__(self, type):
        self.type = type

    def apply(self):
        pass


class Car:

    def __init__(self, registrationNum, year, licenseNumber, engine: Engine, body: Body, gearbox: GearBox, suspension: Suspension, brake: Brake):
        self.registrationNum = registrationNum
        self.year = year
        self.licenseNumber = licenseNumber
        self.gearbox = GearBox
        self.brake = Brake
        self.suspension = Suspension
        self.body = Body
        self.engine = Engine

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


class CarModel(Car):
    def __init__(self, title):
        self.title = title

car = Car(1117, 1989, 54789)

print(car.registrationNum)
print(car.year)
print(car.licenseNumber)



