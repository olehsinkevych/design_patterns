from shopping_cart import ShoppingCart

class CartItem:
    def __init__(self, name: str, product_id: int, quantity: int, until_cost: float, sub_total: float):
        self.name = name
        self.product_id = product_id
        self.quantity = quantity
        self.until_cost = until_cost
        self.sub_total = sub_total

    def new(self, car_id: ShoppingCart()):
        pass

    def calc_price(self):
        pass