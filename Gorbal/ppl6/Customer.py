from OrderFacade import OrderFacade

class Customer:
    def __init__(self):
        self.facade = OrderFacade()
    def orderItem(self, itemName, data):
        self.facade.doOperation("select", itemName)
        self.facade.doOperation("addToCart", itemName)
        if self.facade.doOperation("pay", data):
            self.facade.order.createOrder(self.facade.doOperation("checkout"))
            self.facade.doOperation("ship", itemName)


