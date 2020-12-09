from Person import Person


class Staff(Person):
    def __init__(self, school: str, pay: float, name:str, address:str):
        self.school = school
        self.pay = pay
        super().__init__(name, address)

    @property
    def school(self):
        print("school")

    @school.setter
    def school(self, school):
        self.school = school

    @property
    def pay(self, pay):
        return self.pay

    @pay.setter
    def pay(self, pay):
        self.pay = pay

    def __str__(self):
        return format(str(self._address), str(self._name), str(self.school), float(self.pay))
