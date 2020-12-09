from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def info(self):
        pass


class Bike(Vehicle):
    def __init__(self):
        self.info()

    def info(self):
        print("Це є велосипед")


class Car(Vehicle):
    def __init__(self):
        self.info()

    def info(self):
        print("Це є машина")


class Truck(Vehicle):
    def __init__(self):
        self.info()

    def info(self):
        print("Це є вантажівка")


class Crane(Vehicle):
    def __init__(self):
        self.info()

    def info(self):
        print("Це є кран")
