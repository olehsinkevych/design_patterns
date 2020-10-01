from main import*


v2 = Engine(3.4, 2.4)
Sedan = Body(4)
Sports = Tire(22.8, 0.7)
GearType = GearBoxType("auto", "none")
Mazda = CarModel("mazda")
Tuned = Wheel(17, Sports)
sport = Suspension(184, Tuned)
Metal = Brake("tuned", Tuned)
Gears = GearBox(3, 0, GearType)


mitsubishi = Car(engine=v2, suspension=[sport], body=Sedan, brake=Metal, registration_num=0, year=2018,
                 license_number='0038')

print(mitsubishi.registration_num)