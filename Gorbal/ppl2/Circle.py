from Shape import Shape

class Circle(Shape):
    def __init__(self, color: str, filled: bool,radius: float):
        self._radius = radius
        super().__init__(color, filled)

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,radius):
        self._radius=radius

    def circle(self):
        print("\nCircle\nColor:",self._color," Filled:",self._filled," Radius:",self._radius)