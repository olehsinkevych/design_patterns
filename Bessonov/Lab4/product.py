class Product:
    def __init__(self, product_id: int, name: str, description: str, price: int, image_file_name: str):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.image_file_name = image_file_name

    def display_product(self):
        pass

    def get_product_details(self):
        pass