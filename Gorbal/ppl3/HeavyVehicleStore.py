from  VehicleStore import VehicleStore
from Vehicle import Crane,Truck

class HeavyVehicleStore(VehicleStore):
    def __init__(self):
        self._order_list = []

    def order_vehicle(self, vehicle_type):
        self._order_list.append(vehicle_type)

    def create_vehicle(self, vehicle_type):
        if vehicle_type == "Truck":
            self.order_vehicle(vehicle_type)
            return Truck()
        elif vehicle_type == "Crane":
            self.order_vehicle(vehicle_type)
            return Crane()

    def get_order_list(self):
        return self._order_list