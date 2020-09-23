class GearBox():
    def __init__(self,gear_box_type,gearRatio = [1.0,3.0,5,0], currentGear = 4):
        self.gear_box_type = GearBoxType
        self.__gearRatio = gearRatio
        self.__currentGear = currentGear
    def shift_up(self):
        print("Передача вверх")
    def shift_down(self):
        print("Передача вниз")