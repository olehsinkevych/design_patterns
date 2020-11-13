from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def factory(self):
        pass


class Car(Vehicle):
    def __init__(self):
        self.factory()

    def factory(self):
        print("There is a Car here")

class Bike(Vehicle):
    def __init__(self):
        self.factory()
    def factory(self):
        print("There is a Bike here")

class Truck(Vehicle):
    def __init__(self):
        self.factory()
    def factory(self):
        print("There is a Truck here")

class Crane(Vehicle):
    def __init__(self):
        self.factory()
    def factory(self):
        print("There is a Crane here")
