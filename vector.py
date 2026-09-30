"""Средняя сложность №7. Перегрузка оператора + на примере вектора."""

import math


class Vector:
    """Вектор на плоскости."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        # нужно для sum([v1, v2, ...]): sum начинает с 0 + v1
        if other == 0:
            return Vector(self.x, self.y)
        return self.__add__(other)

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Vector(self.x * number, self.y * number)

    __rmul__ = __mul__

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
