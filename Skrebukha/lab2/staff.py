from person import Person
class Staff(Person):
    def __init__(self,name:str,address:str,school:str,pay:float):
        super().__init__(name,address)
        self.__school = school
        self.__pay = pay
    @property
    def get_school(self):
        return self.__school
    @get_school.setter
    def get_school(self,school:str):
        self.__school = school
    @property
    def get_pay(self):
        return self.__pay
    @get_pay.setter
    def get_pay(self,pay:float):
        self.__pay = pay
    def print_string(self):
        print(self.get_name,self.get_address,self.get_school,self.get_pay,"\n")