class Person():
    def __init__(self,name:str,address:str):
        self.__name = name
        self.__address = address
    @property
    def get_name(self):
        return self.__name
    @property
    def get_address(self):
        return self.__address 
    @get_address.setter
    def get_address(self,address:str):
        self.__address = address
    def print_string(self):
        print(self.get_name,self.get_address,"\n")