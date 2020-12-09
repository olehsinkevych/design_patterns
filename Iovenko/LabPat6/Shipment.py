from ShipmentProvider import ShipmentProvider


class Shipment:
    def __init__(self):
        self.shipments = []
        self.provider = ShipmentProvider()

    def createShipment(self, shipment):
        self.shipments.append(shipment)
        print("Створення замовлення")

    def addProvider(self, provider):
        self.provider.addProvider(provider)
        print("Постачальника додано")
