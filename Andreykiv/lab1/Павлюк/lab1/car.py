class CarModel:
    def __init__(self, title: str):
        self.title = title

class Engine:
    def __init__(self, capacity: float, numberOfCylinders: int):
        self.capacity = capacity
        self.numberOfCylinders = numberOfCylinders
    def start(self):
        print("The Car has started an engine")
    def brake(self):
        print("The engine is stoped")
    def accelerate(self):
        print("Acceleration")

class Body:
    def __init__(self, numberOfDoors: int):
        self.numberOfDoors = numberOfDoors

class GearBox():
    def __init__(self, gearRatio: float, currentGear:int, gearboxtype):
        self.gearRatio = gearRatio
        self.currentGear = currentGear
        self.gearboxtype = gearboxtype
    def shiftUp(self):
        self.currentGear = self.currentGear + self.gearRatio
        print("Current Gear is ", self.currentGear)
    def shiftDown(self):
        self.currentGear = self.currentGear - self.gearRatio
        if self.currentGear < -1:
            print("There are no lower gear")
        else:
            print("Current Gear is ", self.currentGear)

class GearBoxType():
    def __init__(self, name: str, remarks:str):
        self.name = name
        self.remarks = remarks

class Suspension():
    def __init__(self, springRate: float, wheel):
        self.springRate = springRate
        self.wheel = wheel

class Brake():
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
        self.airPreassure = air_preassure


class Car():

    def __init__(self, registration: str, year: int, licenseNumber: str, carmodel, engine, gearbox, body,
                 suspension, brake):
        self.registration = registration
        self.year = year
        self.licenceNumber = licenseNumber
        self.carmodel = carmodel
        self.engine = engine
        self.gearbox = gearbox
        self.body = body
        self.suspension = suspension
        self.brake = brake

    def move_forward(self):
        print("Moving forward")
    def move_backward(self):
        print("Moving backward")
    def stop(self):
        print("The car has stopped")
    def turn_right(self):
        print("turning right")
    def turn_left(self):
        print("turning left")