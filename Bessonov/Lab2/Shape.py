from abc import ABC, abstractmethod


class Shape(ABC):
    '''
    This is super class for shapes
    ...
    Attributes:
        color: str
        filled: bool

    Methods:
        color`s setter and getter
        is_filled`s setter and getter
    '''

    def __init__(self, color:str, filled=True):
        self._color = color
        self._filled = filled

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def filled(self):
        return self.filled

    @filled.setter
    def set_filled(self, filled):
        self.filled = filled

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return'this object is filled {0},color {1}'.format(str(self._color),
                                                           str(self._filled))



