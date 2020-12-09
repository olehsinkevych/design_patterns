from GearBox import gearbox
from Engine import engine
from Suspension import suspension
from Brake import brake
from Body import body
from CarModel import carmodel


class car(gearbox, engine, suspension, brake, body, carmodel):
    def __init__(self, registrnum=int, year=int, licnumb=int):
        self.registration = registrnum
        self.Year = year
        self.Licens = licnumb

    def move_forward(self):
        print("forward")

    def move_backward(self):
        pass

    def stop(self):
        pass

    def turnRight(self):
        pass

    def turnLeft(self):
        pass
