from gearBox import GearBox
from engine import Engine
from suspension import Suspension
from brake import Brake
from body import Body


class Car:
    def __init__(self, registrationNum, year: int, licenseNumber: str, gearBox: GearBox, suspension: Suspension,
                 brake: Brake, body: Body, engine: Engine):
        self.registrationNum = registrationNum
        self.year = year
        self.licenseNumber = licenseNumber
        self.gearBox = gearBox
        self.suspension = suspension
        self.brake = brake
        self.body = body
        self.engine = engine

    def moveForward(self):
        print("move forward")

    def moveBackward(self):
        print("move backward")

    def stop(self):
        print("stop")

    def turnRight(self):
        print("turn right")

    def turnLeft(self):
        print("turn left")
