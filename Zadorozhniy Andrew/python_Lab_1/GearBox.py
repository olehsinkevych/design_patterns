from GearBoxType import gearboxtype


class gearbox(gearboxtype):
    def __init__(self, gear, curgear):
        self.gearRatio = gear
        self.currentGear = curgear

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass
