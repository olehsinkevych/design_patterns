from user import User
from orders import Orders
import copy


class Customer(User):

    def __init__(self, password: str, address: str, email: str, phoneno: int,
                 credit_card_info: str,
                 shipping_info: str):
        super(Customer, self).__init__(password)
        self.customer_name = Orders().customer_name
        self.address = address
        self.email = email
        self.phoneno = phoneno
        self.credit_card_info = credit_card_info
        self.shipping_info = shipping_info

    def register(self):
        pass

    def login(self):
        pass

    def update_profile(self):
        pass

    def search(self):
        pass

    def __copy__(self):
        customer_name = copy.copy(self.customer_name)
        address = copy.copy(self.address)
        email = copy.copy(self.email)
        phoneno = copy.copy(self.phoneno)
        credit_card_info = copy.copy(self.credit_card_info)
        shipping_info = copy.copy(self.shipping_info)

        new = self.__class__(
            super(Customer, self).__init__(self.user_id, self.password, self.login_status), self.customer_name, self.address, self.email, self.phoneno, self.credit_card_info, self.shipping_info
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memodict={}):
        customer_name = copy.deepcopy(self.customer_name)
        address = copy.deepcopy(self.address)
        email = copy.deepcopy(self.email)
        phoneno = copy.deepcopy(self.phoneno)
        credit_card_info = copy.deepcopy(self.credit_card_info)
        shipping_info = copy.deepcopy(self.shipping_info)

        new = self.__class__(
            super(Customer, self).__init__(self.user_id, self.password, self.login_status), self.customer_name,
            self.address, self.email, self.phoneno, self.credit_card_info, self.shipping_info
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return new

    def verify_login(self):
        pass


