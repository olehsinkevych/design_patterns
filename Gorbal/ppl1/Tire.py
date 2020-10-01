class Tire:
    def __init__(self,width:float,air_pressure:float):
        self.width=width
        self.air_pressure=air_pressure

    def display_info_tire(self):
        print("Width =",self.width,"Air pressure =",self.air_pressure)