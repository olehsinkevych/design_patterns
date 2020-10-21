class Engine:
    def __init__(self, capacity: float, number_of_cylindres: int):
        self.capacity = capacity
        self.number_of_cylindres = number_of_cylindres

    def start(self):
        print('start')

    def brake(self):
        print('brake')

    def accelerate(self):
        print('accelerate')