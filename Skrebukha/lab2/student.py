from person import Person
class Student(Person):
    def __init__(self,name:str,address:str,program:str,year:int,fee:float):
        super().__init__(name,address)
        self.__program = program
        self.__year = year
        self.__fee = fee
    @property
    def get_program(self):
        return self.__program
    @get_program.setter
    def get_program(self,program:str):
        self.__program = program
    @property
    def get_year(self):
        return self.__year
    @get_year.setter
    def get_year(self,year:int):
        self.__year = year
    @property
    def get_fee(self):
        return self.__fee
    @get_fee.setter
    def get_fee(self,fee:float):
        self.__fee = fee
    def print_string(self):
        print(self.get_name,self.get_address,self.get_program,self.get_year,self.get_fee,"\n")