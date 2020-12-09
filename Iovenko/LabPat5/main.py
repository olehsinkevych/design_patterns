class BankDetails:
    def __init__(self, bankName: str, accHolderName: str, accNumber: int):
        self.bankName = bankName
        self.accHolderName = accHolderName
        self.accNumber = accNumber

    def setBankName(self, bankName: str):
        self.bankName = bankName

    def getbankName(self):
        return self.bankName

    def setAccHolderName(self, accHolderName: str):
        self.accHolderName = accHolderName

    def getAccHolderName(self):
        return self.accHolderName

    def setAccNumber(self, accNumber: int):
        self.accNumber = accNumber

    def getAccNumber(self):
        return self.accNumber


class BankCustomer(BankDetails):
    def __init__(self, bankName: str, accHolderName: str, accNumber: int):
        super().__init__(bankName, accHolderName, accNumber)

    def giveBankDetails(self):
        print("Назва банку: " + self.bankName + ", Ім'я клієнта: " + \
              self.accHolderName + "Номер клієнта" + str(self.accNumber))

    def getCreditCard(self):
        pass


class CreditCard(BankCustomer):
    def __init__(self, bankName: str, accHolderName: str, accNumber: int):
        super().__init__(bankName, accHolderName, accNumber)

    def giveBankDetails(self):
        pass

    def getCreditCard(self):
        pass
