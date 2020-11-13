from VehicleStore import VehicleStore
from Vehicle import Car,Bike

class LightVehicleStore(VehicleStore):
    def __init__(self):
        self._order_list = []

    def order_vehicle(self, vehicle_type):
        self._order_list.append(vehicle_type)

    def create_vehicle(self, vehicle_type):
        if vehicle_type == "Car":
            self.order_vehicle(vehicle_type)
            return Car()
        elif vehicle_type == "Bike":
            self.order_vehicle(vehicle_type)
            return Bike()

    def get_order_list(self):
        return self._order_list