class Engine():
    def __init__(self,capacity = 10.0,numberOfCylinders = 4):
        self.__capacity = capacity
        self.__numberOfCylinders = numberOfCylinders
    def start(self):
        print("Запуск двигуна")
    def brake(self):
        print("Зупинка")
    def accelerate(self):
        print("Пришвидшення")