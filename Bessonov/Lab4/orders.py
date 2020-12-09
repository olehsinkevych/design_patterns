from order_details import OrderDetails
from shipping_info import ShippingInfo


class Orders:
    def __init__(self, order_id: OrderDetails(), customer_name: str, data_created: str, data_shipped: str, customer_id: str,
                 status: str):

        self.order_id = order_id
        self.data_created = data_created
        self.data_shipped = data_shipped
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.status = status
        self.shipping_id = ShippingInfo().shipping_id

    def place_order(self):
        pass
