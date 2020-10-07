from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,color:str,filled:bool,side:int):
        self._side=side
        super().__init__(color, filled,length=1.0,width=1.0)

    @property
    def side(self):
        return self._side
    @side.setter
    def side(self,side):
        self._side=side

    def square(self):
        print("\nSquare\nColor:",self._color," Filled:",self._filled," Side:",self._side)
