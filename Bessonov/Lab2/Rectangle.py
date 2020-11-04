from Shape import*


class Rectangle(Shape):
    '''
    This class represent a rectangle object
    ...
    Attributes:
        color:str
        filled:bool
        width:float
        height:float
    Methods:
        getters and setters of height and width
        2 methods that find out perimeter and area
    '''
    def __init__(self, color:str, filled: bool, width: float, height: float):
        super().__init__(color, filled)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def get_area(self):
        return self._height * self._width

    def get_perimeter(self):
        return self._height*2 + self._width*2

    def __str__(self):
        return 'This rectangle has color {0}, Is filled? {1}, Width = {2}, Height = {3}'.format(format
                                                                                              (str(self.color),
                                                                                              str(self.filled),
                                                                                              str(self.height),
                                                                                              str(self.width)))

