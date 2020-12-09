from cart_item import CartItem


class ShoppingCart:
    def __init__(self, product_id: CartItem(), quantity: CartItem(), cart_id: int, data_added: int):
        self.cart_id = cart_id
        self.data_added = data_added
        self.product_id = product_id
        self.quantity = quantity

    def add_cart_item(self):
        pass

    def delete_car_item(self):
        pass

    def update_quantity(self):
        pass

    def view_cart_details(self):
        pass

    def checkout(self):
        pass

    def calc_total_price(self):
        pass
