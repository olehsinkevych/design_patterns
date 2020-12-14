class Customer:
    def __init__(self):
        self.facade = OrderFacade()

    def orderItem(self, itemName, data):
        self.facade.doOperation("select", itemName)
        self.facade.doOperation("addToCart", itemName)
        if self.facade.doOperation("pay", data):
            self.facade.order.createOrder(self.facade.doOperation("checkout"))
            self.facade.doOperation("ship", itemName)


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


# inventory
class Stock:
    def __init__(self):
        self.product = Product()
        self.updateStock(["Apple"])

    def selectStockItem(self, index):
        print("Stock item: %s" % self.product.products[index])

    def updateStock(self, stock):
        i = 0
        for item in self.product.products:
            item.updateProduct(i, '')
            i += 1
        for item in stock:
            self.product.addProduct(item)
        print("Updated stock")


class Product:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)
        print("Added product")

    def updateProduct(self, index, product):
        self.products[index] = product
        print("Updated product")


# order process
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


# payment
class Payment:
    def __init__(self):
        self.details = []
        self.details.append("Vasiliy-223322")

    def addCardDetails(self, details):
        self.details.append(details)

    def verifyPayment(self, details):
        for item in self.details:
            if item == details:
                return True
        return False


# shipment
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
        self.addProvider("Egypt")

    def addProvider(self, provider):
        self.providers.append(provider)
        print("Provider created")

    def modifyProvider(self, index, value):
        self.providers[index] = value
        print("Provider modified")


# симуляція роботи
print("Your name: Roman")
Valentin = Customer()
print("You want: an apple")
print("Your credit information: "Vlad Izhak")
Valentin.orderItem("Pineapple", "Vlad Izhak")

