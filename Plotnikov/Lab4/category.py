from product import Product


class Category:
    def __init__(self, category_id: int, department_id: int, category_name: str, description: Product()):
        self.category_id = category_id
        self.department_id = department_id
        self.category_name = category_name
        self.description = description

    def get_products_in_category(self):
        pass
