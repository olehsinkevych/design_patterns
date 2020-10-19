class Person:
    def __init__(self, name: str, address: str):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def Person(self):
        print("Name:", self._name, "\nAddress:", self._address)


class Student(Person):
    def _init_(self, program: str, year: int, fee: float, name=Person.name, address=Person.address):
        self._program = program
        self._year = year
        self._fee = fee
        self.name = name
        self.address = address

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, program):
        self._program = program

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, fee):
        self._fee = fee

    def Student(self):
        print("\nName:", self._name, "\nAddress:", self._address, "\nProgram", self._program,
              "\nYear:", self._year, "\nFee:", self._fee)


class Staff (Person):
    def _init_(self, school: str, pay: float, name=Person.name, address=Person.address):
        self._school = school
        self._pay = pay
        self.name = name
        self.address = address

    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, school):
        self._school = school

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, pay):
        self._pay = pay

    def Staff(self):
        print("\nName:", self._name, "\nAddress:", self._address, "\nSchool:", self._school, "\nPay:", self._pay)