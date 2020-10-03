from car import Car
from engine import Engine
from gear_box import GearBox
from brake import Brake
from suspension import Suspension
from wheel import Wheel
from body import Body

body = Body(2)
wheel = Wheel(10)
engine = Engine(capacity=2, numberOfCylinders=4)
gearBox = GearBox(gearRatio=5, currentGear=3)
brake = Brake(type=4)
suspension = Suspension(springRate=2.0, wheel=wheel)

BlackMercedes = Car(232424319, 2020, '232424319', engine=engine, gear_box=gearBox, brake=brake,
                    suspension=suspension, body=body)
BlackMercedes.name = "auto"
BlackMercedes.remarks = "no comments"
BlackMercedes.gearRatio = "5.36"
BlackMercedes.currentGear = "3"
BlackMercedes.width = 19.5
BlackMercedes.airPressure = 3.4
BlackMercedes.diameter = 7.0
BlackMercedes.type = "4Matic+Coupe"
BlackMercedes.numberOfCylinders = "6"
BlackMercedes.capacity = 17.4
BlackMercedes.numberOfDoors = 2
BlackMercedes.title = "Mercedes"
BlackMercedes.springRate = 2.2

print(BlackMercedes.engine.capacity)