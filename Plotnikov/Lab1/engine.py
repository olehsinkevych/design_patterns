class Engine:
    def __init__(self, capacity: float, number_of_cylinders: int):
        self._capacity = capacity
        self._number_of_cylinders = number_of_cylinders

    def start(self):
        print('Engine has started')

    def brake(self):
        print('Brake has worked')

    def accerate(self):
        print('Accerate has turned on')
