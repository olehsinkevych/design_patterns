from VehicleStore import *

light_factory = LightVehicleStore()
heavy_factory = HeavyVehicleStore()

bike1 = light_factory.create_vehicle("Велосипед")
bike2 = light_factory.create_vehicle("Велосипед")
car = light_factory.create_vehicle("Машина")
truck1 = heavy_factory.create_vehicle("Вантажівка")
crane = heavy_factory.create_vehicle("Кран")
truck2 = heavy_factory.create_vehicle("Вантажівка")

print(light_factory.get_order_list())
print(heavy_factory.get_order_list())
