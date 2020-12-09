from car import Car
from product import Product


class Motoren(Car):
    def __init__(self, product: Product, car_model: str) -> None:
        super().__init__(product, car_model)
        self.product = product
        self.car_model = car_model

    def assemble(self):
        print("Assembling Motoren...")

    def build_product(self):
        return print(f"{self.product.product_name} for {self.car_model} building\n"
                     f"{self.product.product_name} for {self.car_model} is done\n")
