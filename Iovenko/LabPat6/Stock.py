from Product import Product


class Stock:
    def __init__(self):
        self.product = Product()
        self.updateStock(["Кавун"])

    def selectStockItem(self, index):
        print("Продукт запасу: %s" % self.product.products[index])

    def updateStock(self, stock):
        i = 0
        for item in self.product.products:
            item.updateProduct(i, '')
            i += 1
        for item in stock:
            self.product.addProduct(item)
        print("Поновлено запаси")
