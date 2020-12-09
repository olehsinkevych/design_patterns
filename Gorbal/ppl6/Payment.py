class Payment:
    def __init__(self):
        self.details = []
        self.details.append("Vasiliy-223322")
    def addCardDetails(self, details):
        self.details.append(details)
    def verifyPayment(self, details):
        for item in self.details:
            if item == details:
                return True
        return False


