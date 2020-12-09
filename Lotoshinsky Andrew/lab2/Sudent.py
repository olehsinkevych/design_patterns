from Person import Person


class Student(Person):
    def __init__(self, program: str, year: int, fee: float, name:str, address:str):
        self.program = program
        self.year = year
        self.fee = fee
        super().__init__(name, address)

    @property
    def program(self):
        return self.program

    @program.setter
    def program(self, program):
        self.program = program

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, year):
        self.year = year

    @property
    def fee(self, fee):
        return self.fee

    @fee.setter
    def fee(self, fee):
        self.fee = fee

    def __str__(self):
        return format(str(self._address), str(self._name), int(self.year), float(self.fee))
