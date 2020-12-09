class Product:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)
        print("Добавлено продукт")

    def updateProduct(self, index, product):
        self.products[index] = product
        print("Оновлений продукт")
