import math


class Ball:

    def __init__(self, x: float, y: float, radius: int, speed: int, direction: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = direction
        self.x_delta = self._speed * math.cos(self._direction)
        self.y_delta = -self._speed * math.sin(self._direction)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    @property
    def x_delta(self):
        return self._x_delta

    @x_delta.setter
    def x_delta(self, x_delta):
        self._x_delta = x_delta

    @property
    def y_delta(self):
        return self._y_delta

    @y_delta.setter
    def y_delta(self, y_delta):
        self._y_delta = y_delta

    def move(self):
        self._x += self._x_delta
        self._y += self._y_delta

    def reflect_horizontal(self):
        self._x_delta = -self._x_delta

    def reflect_vertical(self):
        self._y_delta = -self._y_delta

    def __str__(self):
        return f"Ball at {self._x, self._y} of velocity {self._x_delta, self._y_delta}"
