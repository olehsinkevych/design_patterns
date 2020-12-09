from abc import abstractmethod
from product import Product


class Car:
    def __init__(self, product: Product, car_model: str) -> None:
        self.product = product
        self.car_model = car_model

    @abstractmethod
    def assemble(self):
        pass

    @abstractmethod
    def build_product(self):
        pass

    def __str__(self):
        return f"Product: {self.product.product_name()}\n" \
               f"Car model: {self.car_model}\n"
