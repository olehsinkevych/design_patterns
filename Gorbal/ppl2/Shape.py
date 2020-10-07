class Shape:
    def __init__(self,color:str,filled:bool):
        self._color=color
        self._filled=filled

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color=color

    @property
    def filled(self):
        return self._filled
    @filled.setter
    def filled(self,filled):
        self._filled=filled

    def shape(self):
        print("Shape\nColor:",self._color," Filled:",self._filled)