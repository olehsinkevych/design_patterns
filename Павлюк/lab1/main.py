from car import*

V2 = Engine(3.2, 2.0)
Sedan = Body(4)
Sports = Tire(22.8, 0.7)
GearType = GearBoxType("auto", "none")
Lancer = CarModel("Lancer")
Tuned = Wheel(17, Sports)
Sport = Suspension(228, Tuned)
Metal = Brake("tuned", Tuned)
Gears = GearBox(3, 0, GearType)
Mitsubishi = Car("1990", 1989, "AT 6666 AE", Lancer, V2, GearType, Sedan, Sports, Metal)

print(Gears.gearRatio)