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
