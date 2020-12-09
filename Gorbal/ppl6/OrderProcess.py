class ShoppingCart:
    def __init__(self):
        self.items = {}
    def addItem(self, item, amount=1):
        self.items[item] = 1
        print("Added item")
        if amount != 1:
            self.updateAmount(item, amount)
    def updateAmount(self, item, amount):
        self.items[item] = amount
        print("Updated amount")
    def checkout(self):
        for item in self.items:
            print("Item: " + str(item) + " Amount: " + str(self.items[item]))
            return "Item: " + str(item) + " Amount: " + str(self.items[item])


class Order:
    def __init__(self):
        self.orders = []
    def createOrder(self, order):
        self.orders.append(order)
        print("Order created")
    def editOrder(self, index, order):
        self.orders[index] = order
        print("Order updated")
