class Car():
    def __init__(self,engine,gear_box,body,suspension,brake,registrationNum,year = 2019,licenseNumber = "poroshenko"):
        self.engine = Engine
        self.gear_box = GearBox
        self.body = Body
        self.suspension = Suspension
        self.brake = Brake
        self.__registrationNum = registrationNum
        self.__year = year
        self.__licenseNumber = licenseNumber
    def move_forward(self):
        print("рух у перід")
    def move_backward(self):
        print("задній хід")
    def stop(self):
        print("Зупинка")
    def turn_right(self):
        print("Поворот у право")
    def turn_left(self):
        print("Поворот у ліво")