class Order:
    def __init__(self):
        self.orders = []

    def createOrder(self, order):
        self.orders.append(order)
        print("Замовлення створено")

    def editOrder(self, index, order):
        self.orders[index] = order
        print("Замовлення отримано")
