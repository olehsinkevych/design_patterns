from abc import ABC,abstractmethod

class VehicleStore(ABC):
    @abstractmethod
    def order_vehicle(self, vehicle_type):
        pass
    @abstractmethod
    def create_vehicle(self, vehicle_type):
        pass




