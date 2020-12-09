from OrderFacade import OrderFacade


class Customer:
    def __init__(self):
        self.facade = OrderFacade()

    def orderItem(self, itemName, data):
        self.facade.doOperation("вибрати", itemName)
        self.facade.doOperation("добавити у кошик", itemName)
        if self.facade.doOperation("заплатити", data):
            self.facade.order.createOrder(self.facade.doOperation("поновити"))
            self.facade.doOperation("доставити", itemName)
