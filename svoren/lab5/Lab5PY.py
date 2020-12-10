import abc

class CreditCard(abc.ABC):
    @abc.abstractmethod
    def give_bank_details(self) -> None:
        pass
    @abc.abstractmethod
    def get_credit_card(self) -> str:
        pass

class BankDetails():
    def __init__(self,bank_name="ПриватБанк",acc_holder_name="Ярослав Сворень",acc_number=5168123456780923):
        self._bank_name = bank_name
        self._acc_holder_name = acc_holder_name
        self._acc_number = acc_number
    @property
    def get_bank_name(self):
        return self._bank_name
    @get_bank_name.setter
    def get_bank_name(self,bank_name):
        self._bank_name = bank_name
    @property
    def get_acc_holder_name(self):
        return self._acc_holder_name
    @get_acc_holder_name.setter
    def get_acc_holder_name(self,acc_holder_name):
        self._acc_holder_name = acc_holder_name
    @property
    def get_acc_number(self):
        return self._acc_number
    @get_acc_number.setter
    def get_acc_number(self,acc_number):
        self._acc_nmuber = acc_number    

class BankCustomer(CreditCard,BankDetails):
    def give_bank_details(self) -> None:
        print(self.get_bank_name)
        print(self.get_acc_holder_name)
    def get_credit_card(self) -> str:
        return self.get_acc_number

class Adapter(CreditCard):
    def __init__(self,adapter:BankDetails):
        self.customer = adapter
    def give_bank_details(self) -> None:
        print(self.customer.get_bank_name)
        print(self.customer.get_acc_holder_name)
    def get_credit_card(self) -> str:
        return self.customer.get_acc_number

yaroslav1 = BankCustomer()
print(yaroslav1.get_bank_name)
print(yaroslav1.get_acc_holder_name)
print(yaroslav1.get_acc_number,"\n")
neyaroslav1 = BankDetails("Альфа Банк","НеЯрослав Сворень",5355329087654321)
yaroslav2 = Adapter(neyaroslav1)
yaroslav2.give_bank_details()
print(yaroslav2.get_credit_card())