from car import Car
from carModel import CarModel
from gearBox import GearBox
from engine import Engine
from suspension import Suspension
from body import Body
from brake import Brake

carModel = CarModel("Tesla")
gearBox = GearBox(5, 3, "auto")
engine = Engine(1.9, 6)
suspension = Suspension(3, "Chrome Coated")
body = Body(4)
brake = Brake("Disc", suspension.wheel)

whiteOpel = Car(232424324, 2020, "23434234", gearBox, suspension, brake, body, engine)
whiteOpel.turnLeft()
whiteOpel.moveBackward()
whiteOpel.stop()
gearBox.shifDown()
gearBox.shiftUp()
engine.start()
engine.brake()
