from  GearBoxType import GearBoxType

class GearBox:
    def __init__(self,gear_ratio:float,current_gear:int):
        self.gear_ratio=gear_ratio
        self.current_gear=current_gear

    def shift_up(self):
        return self.shift_up
    def shift_down(self):
        return self.shift_down

    def display_info_gb(self):
        print("Gear ratio =",self.gear_ratio,"Current gear =",self.current_gear)

    my_car=GearBoxType('Ruslan_Gorbal',1)
    my_car.display_info_gbt()