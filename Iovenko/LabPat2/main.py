class Person:
    def __init__(self, name: str, adress: str):
        self.name = name
        self.adress = adress

    def get_Name(self):
        return self.name

    def get_Adress(self):
        return self.adress

    def set_Adress(self, adress: str):
        self.adress = adress

    def __str__(self):
        return "Person -  [name = " + self.name + ", adress = " + self.adress + "]"


class Staff(Person):
    def __init__(self, name: str, adress: str, school: str, pay: float):
        super().__init__(name, adress)
        self.school = school
        self.pay = pay

    def get_School(self):
        return self.school

    def set_School(self, school: str):
        self.school = school

    def get_Pay(self):
        return self.pay

    def set_Pay(self, pay: float):
        self.pay = pay

    def __str__(self):
        return "Staff -   [Person [name = " + self.name + ", adress = " + self.adress + "], school = " \
               + self.school + ", pay = " + str(self.pay) + "$]"


class Student(Person):
    def __init__(self, name: str, adress: str, program: str, year: int, fee: float):
        super().__init__(name, adress)
        self.program = program
        self.year = year
        self.fee = fee

    def get_Program(self):
        return self.program

    def set_Program(self, program: str):
        self.program = program

    def get_Year(self):
        return self.year

    def set_Year(self, year: int):
        self.year = year

    def get_Fee(self):
        return self.fee

    def set_Fee(self, fee: float):
        self.fee = fee

    def __str__(self):
        return "Student - [Person [name = " + self.name + ", adress = " + self.adress + \
               "], program = " + self.program + ", year = " + str(self.year) + ", fee = " + str(self.fee) + "$]"


mypers = Person("Arsen", "Kyiv")
print(mypers)

myStaff = Staff("Dima", "Dnipro", "Dnipro_School", 500)
print(myStaff)

mystudent = Student("Oleh", "Lviv", "Electronik", 2020, 200)
print(mystudent)
