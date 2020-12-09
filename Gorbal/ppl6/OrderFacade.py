from OrderProcess import Order,ShoppingCart
from Shipment import Shipment, ShipmentProvider
from Inventory import Stock,Product
from Payment import Payment


class OrderFacade:
    def __init__(self):
        self.stock = Stock()
        self.shoppingCart = ShoppingCart()
        self.order = Order()
        self.shipment = Shipment()
        self.payment = Payment()

    def doOperation(self, name, value=''):
        if name == "select":
            index = -1
            for item in self.stock.product.products:
                index += 1
                if item == value:
                    self.stock.selectStockItem(index)
        elif name == "addToCart":
            self.shoppingCart.addItem(value)
        elif name == "order":
            self.shoppingCart.addItem(value)
        elif name == "ship":
            self.shipment.createShipment(value)
        elif name == "pay":
            if self.payment.verifyPayment(value):
                print("Payment verified")
                return True
            else:
                if input("Unknown card data, want to register a card?\n") == "yes":
                    self.payment.addCardDetails(value)
                    print("Payment verified")
                    return True
                else:
                    return False
        elif name == "checkout":
            self.shoppingCart.checkout()
