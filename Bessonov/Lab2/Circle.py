from Shape import*
import math


class Circle(Shape):
    '''
    This object represents a circle
    ...
    Attributes:
        Color: str
        Filled: bool
        Radius: float
    '''
    def __init__(self, color:str, filled:bool, radius:float):
        super().__init__(color, filled)
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def set_radius(self, radius):
        self._radius = radius


    def get_area(self):
        ''' This Method shows area off  circle object'''
        return math.pi * self._radius**2

    def get_perimeter(self):
        ''' This Method show perimeter off circle object'''
        return self._radius**2

    def __str__(self):
        return 'This circle has color {0}, Is filled? {1}, Radius = {2}'.format(str(self._color),
                                                                                              str(self._filled),
                                                                                              str(self._radius))
