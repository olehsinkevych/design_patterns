from Shape import Shape

class Rectangle(Shape):
    def __init__(self,color: str,filled: bool,width:float, length:float):
        self._width=width
        self._length=length
        super().__init__(color, filled)

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        self._width=width

    @property
    def length(self):
        return self._length
    @length.setter
    def length(self,length):
        self._length=length

    def rectangle(self):
        print("\nRectangle\nColor:",self._color," Filled:",self._filled," Width:",self._width," Length:",self._length)
