from user import User


class Administrator(User):
    def __init__(self, password: str, admin_name: str, email: str):
        super(Administrator, self).__init__(password)
        self.admin_name = admin_name
        self.email = email

    def verify_login(self):
        pass

    def create_department(self):
        pass

    def create_category(self):
        pass

    def create_product(self):
        pass

    def delete_department(self):
        pass

    def delete_category(self):
        pass

    def delete_product(self):
        pass

    def edit_catalog_details(self):
        pass
