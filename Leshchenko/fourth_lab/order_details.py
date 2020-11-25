class OrderDetails:
    def __init__(self, order_id: int, product_id: int, product_name: str, quantity: int, until_cost: float,
                 sub_total: float):
        self.order_id = order_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.until_cost = until_cost
        self.sub_total = sub_total

    def calc_price(self):
        pass
