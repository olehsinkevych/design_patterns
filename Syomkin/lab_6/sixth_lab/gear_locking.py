from product import Product


class GearLocking(Product):
    def __init__(self, product_name: str) -> None:
        self.product_name = product_name

    def product_name(self):
        return self.product_name

    def build(self):
        return "Method build() in GearLocking class invoked"
