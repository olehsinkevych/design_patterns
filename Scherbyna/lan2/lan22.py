class Person:
    def __init__(self,name = str,address=str):
        self._name = name
        self._address = address
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self,address):
        self._address=address
    def Person(self):
        print(self._address,'',self._name)
        


class Student(Person):
    def __init__ (self,program=str,year=int,fee=float, name=Person.name, address=Person.address):
        self.program=program
        self.year=year
        self.fee=fee
    @property
    def program(self):
        return self.program
    @program.setter
    def program(self,program):
        self.program=program
    @property
    def year(self):
        return self.year
    @year.setter
    def year(self,year):
        self.year=year
    @property
    def fee(self):
        return self.fee
    @fee.setter
    def fee(self,fee):
        self.fee=fee
    def string(self):
        print(self.program,'',self.year,'',self.fee,'',self.name,'',self.address)
    

class Staff(Person):
    def __init__ (self,school=str,pay=float,name=Person.name,address=Person.address):
    self.school=school
    self.pay=pay
    @property
    def school(self):
        return self.school
    @school.setter
    def school(self,school):
        self.school=school
    @property
    def pay(self):
        return self.pay
    @pay.setter
    def pay(self,pay):
        self.pay=pay
    def string(self):
        print(self.school,'',self.pay,'',self.name,'',self.address)