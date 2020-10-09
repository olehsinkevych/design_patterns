from gearBoxType import GearBoxType


class GearBox():
    def __init__(self, gearRatio, currentGear, type: GearBoxType):
        self.gearRatio = gearRatio
        self.currentGear = currentGear
        self.type = type

    def shiftUp(self):
        print("shift up")

    def shifDown(self):
        print("shift down")
