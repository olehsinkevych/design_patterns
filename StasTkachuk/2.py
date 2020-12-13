

class Person:
    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address

    @property
    def get_name(self):
        return self.__name

    @property
    def get_address(self):
        return self.__address

    @get_address.setter
    def get_address(self, address: str):
        self.__address = address

    def to_string(self):
        print("Person[", self.get_name, ", ", self.get_address, "]", sep="")


class Student(Person):
    def __init__(self, program: str, year: int, fee: float):
        self.__program = program
        self.__year = year
        self.__fee = fee

    @property
    def get_program(self):
        return self.__program

    @get_program.setter
    def get_program(self, program: str):
        self.__program = program

    @property
    def get_year(self):
        return self.__year

    @get_year.setter
    def get_year(self, year: int):
        self.__year = year

    @property
    def get_fee(self):
        return self.__fee

    @get_fee.setter
    def get_fee(self, fee: float):
        self.__fee = fee

    def to_string(self):
        print("Program: ", self.get_program, ", year: ", self.get_year, ", fee: ", self.get_fee, sep="")


class Staff(Person):
    def __init__(self, school: str, pay: float):
        self.__school = school
        self.__pay = pay

    @property
    def get_school(self):
        return self.__school

    @get_school.setter
    def get_school(self, school: str):
        self.__school = school

    @property
    def get_pay(self):
        return self.__pay

    @get_pay.setter
    def get_pay(self, pay: float):
        self.__pay = pay

    def to_string(self):
        print("school: ", self.get_school, ", pay: ", self.get_pay, sep="")


x1 = Person("Станіслав", "Прикордонників")
x1.to_string()
x2 = Student("IT", 2019, 30500.0)
x2.to_string()
x3 = Staff("LNU", 31100.0)
print("Перевірка сеттеру:")
x3.get_pay = 86755.8
x3.to_string()