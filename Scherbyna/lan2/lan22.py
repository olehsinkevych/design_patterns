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
    def __init__ (self,name ,address ,program=str,year=int,fee=float):
        super().__init__(name, address)
        self._program=program
        self._year=year
        self._fee=fee
    @property
    def program(self):
        return self._program
    @program.setter
    def program(self,program):
        self._program=program
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self,year):
        self._year=year
    @property
    def fee(self):
        return self._fee
    @fee.setter
    def fee(self,fee):
        self._fee=fee
    def string(self):
        print(self._name,'',self._address,'',self._program,'',self._year,'',self._fee)
    

class Staff(Person):
    def __init__ (self, name ,address,school=str,pay=float):
        super().__init__(name, address)
        self._school=school
        self._pay=pay
    @property
    def school(self):
        return self._school
    @school.setter
    def school(self,school):
        self._school=school
    @property
    def pay(self):
        return self._pay
    @pay.setter
    def pay(self,pay):
        self._pay=pay
    def string(self):
        print(self._name,'',self._address,'',self._school,'',self._pay)

