from Rectangle import *


class Square(Rectangle):
    '''
    This class represents square
    ...
    Attributes:
        color:str
        filled:bool
        width:float
    Methods:
        getters and setters of width attribute
        get_area and get_perimeter methods to get area and perimeter of square object
        __str__ method to get all information about square object
    '''
    def __init__(self, color: str, filled: bool, width: float):
        super().__init__(color, filled, width)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    def get_area(self):
        return self._width*self._width

    def get_perimeter(self):
        return self._width*4

    def __str__(self):
        return  'This square has color {0}, Is filled? {1}, Width = {2}'.format(format
                                                                                              (str(self._color),
                                                                                              str(self._filled),
                                                                                              str(self._width)))
