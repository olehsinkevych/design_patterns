class Shipment:
    def __init__(self):
        self.shipments = []
        self.provider = ShipmentProvider()
    def createShipment(self, shipment):
        self.shipments.append(shipment)
        print("Shipment created")
    def addProvider(self, provider):
        self.provider.addProvider(provider)
        print("Provider added")


class ShipmentProvider:
    def __init__(self):
        self.providers = []
        self.addProvider("Belgium")
    def addProvider(self, provider):
        self.providers.append(provider)
        print("Provider created")
    def modifyProvider(self, index, value):
        self.providers[index] = value
        print("Provider modified")
