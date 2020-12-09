from car import Car
from product import Product


class BigWheel(Car):
    def __init__(self, product: Product, car_model: str) -> None:
        super().__init__(product, car_model)
        self.product = product
        self.car_model = car_model

    def assemble(self):
        return print("Assembling Big Wheel...")

    def build_product(self):
        return print(f"{self.product.product_name} for {self.car_model} building\n"
                     f"{self.product.product_name} for {self.car_model} is done\n")

    def __str__(self):
        return super.__str__(self.product)
