from  LightVehicleStore import LightVehicleStore
from HeavyVehicleStore import HeavyVehicleStore

light_factory = LightVehicleStore()
heavy_factory = HeavyVehicleStore()

car1 = light_factory.create_vehicle("Car")
truck = heavy_factory.create_vehicle("Truck")
bike1 = light_factory.create_vehicle("Bike")
bike2 = light_factory.create_vehicle("Bike")
truck2 = heavy_factory.create_vehicle("Truck")
car2 = light_factory.create_vehicle("Car")
crane = heavy_factory.create_vehicle("Crane")


print(light_factory.get_order_list())
print(heavy_factory.get_order_list())