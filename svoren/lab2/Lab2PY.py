class Person():
    def __init__(self,name="Ivan",address="Universitetska 1"):
        self.__name = name
        self.__address = address
    @property
    def get_name(self):
        return self.__name
    @property
    def get_address(self):
        return self.__address 
    @get_address.setter
    def set_address(self,address:str):
        self.__address = address
    def to_string(self):
        print("Person",self.get_name + ",",self.get_address)

class Student(Person):
    def __init__(self,name="Ivan",address="Universitetska 1",program="Software Engineering",year=2020,fee=31103.5):
        super().__init__(name,address)
        self.__program = program
        self.__year = year
        self.__fee = fee
    @property
    def get_program(self):
        return self.__program
    @get_program.setter
    def set_program(self,program:str):
        self.__program = program
    @property
    def get_year(self):
        return self.__year
    @get_year.setter
    def set_year(self,year:int):
        self.__year = year
    @property
    def get_fee(self):
        return self.__fee
    @get_fee.setter
    def set_fee(self,fee:float):
        self.__fee = fee
    def to_string(self):
        print("Student",self.get_name + ",",self.get_address + ",",self.get_program + ",",str(self.get_year) + ",",str(self.set_fee))

class Staff(Person):
    def __init__(self,name="Ivan",address="Universitetska 1",school="Ivan Franko University of Lviv",pay=15675.5):
        super().__init__(name,address)
        self.__school = school
        self.__pay = pay
    @property
    def get_school(self):
        return self.__school
    @get_school.setter
    def set_school(self,school:str):
        self.__school = school
    @property
    def get_pay(self):
        return self.__pay
    @get_pay.setter
    def set_pay(self,pay:float):
        self.__pay = pay
    def to_string(self):
        print("Staff",self.get_name + ",",self.get_address+",",self.get_school+",",str(self.get_pay))

whaddup = Person()
whaddup.to_string()
print("\n")
whaddup2 = Student("Yaroslav","Liberty Avenue 19")
whaddup2.to_string()
print("\n")
whaddup3 = Staff("Oleh","Dragomanova 50")
whaddup3.to_string()