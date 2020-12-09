class ShoppingCart:
    def __init__(self):
        self.items = {}

    def addItem(self, item, amount=1):
        self.items[item] = 1
        print("Добавлено продукт")
        if amount != 1:
            self.updateAmount(item, amount)

    def updateAmount(self, item, amount):
        self.items[item] = amount
        print("оновлена к-сть")

    def checkout(self):
        for item in self.items:
            print("Продукт: " + str(item) + " к-сть: " + str(self.items[item]))
            return "Продукт: " + str(item) + " к-сть: " + str(self.items[item])
