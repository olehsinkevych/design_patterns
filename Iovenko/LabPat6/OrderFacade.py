from Stock import Stock
from ShoppingCart import ShoppingCart
from Order import Order
from Shipment import Shipment
from Payment import Payment


class OrderFacade:
    def __init__(self):
        self.stock = Stock()
        self.shoppingCart = ShoppingCart()
        self.order = Order()
        self.shipment = Shipment()
        self.payment = Payment()

    def doOperation(self, name, value=''):
        if name == "вибрати":
            index = -1
            for item in self.stock.product.products:
                index += 1
                if item == value:
                    self.stock.selectStockItem(index)
        elif name == "добавити у кошик":
            self.shoppingCart.addItem(value)
        elif name == "замовлення":
            self.shoppingCart.addItem(value)
        elif name == "доставити":
            self.shipment.createShipment(value)
        elif name == "заплатити":
            if self.payment.verifyPayment(value):
                print("Підтвердження оплати")
                return True
            else:
                if input("Не існує картки, бажаєте зареєструвати одну?\n") == "так":
                    self.payment.addCardDetails(value)
                    print("Підтвердження оплати")
                    return True
                else:
                    return False
        elif name == "поновити":
            self.shoppingCart.checkout()
