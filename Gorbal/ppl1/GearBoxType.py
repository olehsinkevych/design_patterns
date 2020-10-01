class GearBoxType:
    def __init__(self,name,remarks):
        self.name=name
        self.remarks=remarks

    def display_info_gbt(self):
        print("Lab",self.remarks,"has completed by",self.name)