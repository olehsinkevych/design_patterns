from gearBoxType import GearBoxType


class GearBox(GearBoxType):
    def __init__(self, gear_ratio: float, current_gear: int):
        self.gear_ratio = gear_ratio
        self.current_gear = current_gear

    def shiftUp(self):
        print('shiftUp')

    def shiftDown(self):
        print('shiftDown')