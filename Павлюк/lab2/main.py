""""""
from abc import ABC, abstractmethod, ABCMeta
import math


class Shape(metaclass=ABCMeta):
    def __init__(self, color: str, filled: bool) -> None:
        self.color = color
        self.filled = filled

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Shape {self.color}, {self.filled}"


class Circle(Shape):
    def __init__(self, radius=1, color='red', filled=True) -> None:
        super().__init__(color, filled)
        self._radius = radius

    @property
    def radius(self):
        return  self._radius

    @radius.setter
    def radius(self, radius):
        assert radius > 0
        self._radius = radius

    def get_area(self) -> float:
        return math.pi * self._radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def __str__(self):
        return f'Rectangle {self.color}, {self.filled}, radius {self._radius}'


class Rectangle(Shape):
    def __init__(self, length=1, width=1, color='red', filled=True):
        super().__init__(color=color, filled=filled)
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        assert length > 0
        self._length = length

    def get_perimeter(self) -> float:
        pass

    def get_area(self) -> float:
        pass

    def __str__(self):
        pass


class Square(Rectangle):
    def __init__(self, side=1, color='red', filled=True):
        super().__init__(length=side, width=side, color=color, filled=filled)

    @property
    def side(self):
        return self.length

    @side.setter
    def side(self, side):
        self.length = side


circle = Circle()
print(circle)