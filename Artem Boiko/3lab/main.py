from abc import ABC, abstractmethod


# VehicleStore
class VehicleStore(ABC):
    @abstractmethod
    def order_vehicle(self, vehicle_type):
        pass

    @abstractmethod
    def create_vehicle(self, vehicle_type):
        pass


# Vehicle Interface
class Vehicle(ABC):
    @abstractmethod
    def factory_method(self):
        pass


class Bike(Vehicle):
    def __init__(self):
        self.factory_method()

    def factory_method(self):
        print("Bike")


class Car(Vehicle):
    def __init__(self):
        self.factory_method()

    def factory_method(self):
        print("Car")


class Truck(Vehicle):
    def __init__(self):
        self.factory_method()

    def factory_method(self):
        print("Truck")


class Crane(Vehicle):
    def __init__(self):
        self.factory_method()

    def factory_method(self):
        print("Crane")


# LightVehicleStore
class LightVehicleStore(VehicleStore):
    def order_vehicle(self, vehicle_type):
        pass

    def create_vehicle(self, vehicle_type):
        if vehicle_type == "Car":
            car = Car()
        elif vehicle_type == "Bike":
            bike = Bike()


# HeavyVehicleStore
class HeavyVehicleStore(VehicleStore):
    def order_vehicle(self, vehicle_type):
        pass

    def create_vehicle(self, vehicle_type):
        if vehicle_type == "Truck":
            truck = Truck()
        elif vehicle_type == "Crane":
            crane = Crane()


# light_factory = LightVehicleStore()
# heavy_factory = HeavyVehicleStore()

# Bike Car Truck Crane
bike = LightVehicleStore()
bike.create_vehicle("Bike")
car = LightVehicleStore()
car.create_vehicle("Car")
truck = HeavyVehicleStore()
truck.create_vehicle("Truck")
crane = HeavyVehicleStore()
crane.create_vehicle("Crane")
