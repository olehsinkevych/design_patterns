from ball import Ball


class Container:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width - 1
        self.y2 = y + height - 1

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __str__(self):
        return f"Container at {self.x1, self.y1} to {self.x2, self.y2}"

    def collides_with(self, ball: Ball):
        if self.x2 <= (ball.x + ball.radius) or (ball.x - ball.radius) <= self.x1:
            ball.reflect_horizontal()
        if self.y2 <= (ball.y + ball.radius) or (ball.y - ball.radius) <= self.y1:
            ball.reflect_vertical()