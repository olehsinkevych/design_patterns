class ShipmentProvider:
    def __init__(self):
        self.providers = []
        self.addProvider("Туреччина")

    def addProvider(self, provider):
        self.providers.append(provider)
        print("Постачальника створено")

    def modifyProvider(self, index, value):
        self.providers[index] = value
        print("Постачальника змінено")
