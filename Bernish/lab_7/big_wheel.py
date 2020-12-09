from car import Car
from product import Product


class BigWheel(Car):
    def __init__(self, product: Product, car_model: str) -> None:
        super().__init__(product, car_model)
        self.product = product
        self.car_model = car_model

    def assemble(self):
        print("Сборка Big Wheel...")

    def build_product(self):
        print( str(self.product.product_name) +" для "  + self.car_model +  " будується\n"
                     + str(self.product.product_name) + " для " + self.car_model + " готовий\n")

    def __str__(self):
        super.__str__(self.product)
