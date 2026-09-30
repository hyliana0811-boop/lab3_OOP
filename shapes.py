"""Средняя сложность №4. Класс «Фигура» (площадь, периметр) и наследники."""

import math


class Shape:
    """Базовая фигура. Наследники обязаны переопределить area и perimeter."""

    name = "фигура"

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def describe(self):
        return (f"{self.name}: площадь {self.area():.2f}, "
                f"периметр {self.perimeter():.2f}")

    def __repr__(self):
        return f"<{self.__class__.__name__} S={self.area():.2f}>"


def _check_positive(*values):
    for value in values:
        if value <= 0:
            raise ValueError("Размеры фигуры должны быть положительными")


class Circle(Shape):
    name = "круг"

    def __init__(self, radius):
        _check_positive(radius)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    name = "прямоугольник"

    def __init__(self, width, height):
        _check_positive(width, height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    name = "квадрат"

    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Shape):
    name = "треугольник"

    def __init__(self, a, b, c):
        _check_positive(a, b, c)
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a, self.b, self.c = a, b, c

    def area(self):
        # формула Герона
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
