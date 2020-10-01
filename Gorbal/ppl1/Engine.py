class Engine:
    def __init__(self,capacity:float,number_cylinders:int):
        self.capacity=capacity
        self.number_cylinders=number_cylinders
    def start(self):
        return self.start
    def brake(self):
        return self.brake
    def accerate(self):
        return self.accerate

    def display_info_engine(self):
        print("Capacity of motor =",self.capacity,"Number of cylinders =",self.number_cylinders)
