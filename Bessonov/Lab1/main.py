from carparts import *
from carbody import*



V228 = Engine(3.5, 228)
Sedan = Body(4)
Shirokie = Tire(22.8, 0.7)
TypeGear = GearBoxType("automat", "none")
E34 = CarModel("E34")
Big = Wheel(19, Shirokie)
Sport = Suspension(228, Big)
Titan = Brake("horoshie", Big)
Gear = GearBox(7, 0, TypeGear)
BMW = Car("1990", 1989, "BO 777 P", E34, V228, Gear, Sedan, Sport, Titan)


