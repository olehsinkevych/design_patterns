from GearBox import GearBox
from GearBoxType import GearBoxType
from Suspension import Suspension
from Body import Body
from Tire import Tire
from Wheel import Wheel
from Brake import Brake
from lab1 import Car
from CarModel import CarModel
from engine import Engine


engine = Engine(capacity=2, number_of_cylinders=4)
car_model = CarModel()
gear_box_type = GearBoxType(name='', remarks='')
suspension = Suspension(spring_rate=0.0)
body = Body(number_of_doors=4)
wheel = Wheel(diameter=18)
gear_box = GearBox(gear_ratio=1.2, current_gear=3)
tire = Tire(width=12, air_pressure=14)
brake = Brake(type='brembo')


car = Car(registration_num=8457, year=2015, license_number='XCSSERRS', engine=engine, gear_box=gear_box, gear_box_type=gear_box_type,
          suspension=suspension, body=body, tire=tire, wheel=wheel, brake=brake)

print(car.engine._capacity)
print(car.brake.apply())
print(car._registration_num)
print(car._license_number)
