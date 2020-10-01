from car import CarModel, Car, GearBox, Engine, Suspension, Brake, Body

car_model = CarModel("BMW")
car_model.model()

gear_box = GearBox(1, 1)
gear_box.gear_ratio = 1

eng = Engine(1.9, 6)

suspension = Suspension(4)
body = Body(4)
brake = Brake(5)

car = Car("123", 5, "UA83929824", engine=eng, suspension=suspension, number_of_doors=body, brake=brake)
car.car_info()
eng.car_engine()
eng.start()
gear_box.car_gear()
car.move_forward()
gear_box.shift_up()
gear_box.car_gear()
eng.accelerate()
car.move_backward()
gear_box.shift_down()
gear_box.car_gear()
car.stop()

