"""Повышенная сложность №6. Наследование от list с доп. методами."""

from shapes import Shape


class ShapeList(list):
    """Список, в котором могут храниться только фигуры (Shape).

    Все обычные возможности list сохраняются, а проверка типа добавлена
    в методы, через которые элементы попадают в список.
    """

    def __init__(self, items=()):
        super().__init__()
        self.extend(items)

    @staticmethod
    def _check(item):
        if not isinstance(item, Shape):
            raise TypeError(f"В ShapeList можно добавить только фигуру, "
                            f"получено: {type(item).__name__}")
        return item

    def append(self, item):
        super().append(self._check(item))

    def insert(self, index, item):
        super().insert(index, self._check(item))

    def extend(self, items):
        super().extend(self._check(item) for item in items)

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            value = [self._check(item) for item in value]
        else:
            value = self._check(value)
        super().__setitem__(index, value)

    def __iadd__(self, items):
        self.extend(items)
        return self

    # --- дополнительные методы ---

    def total_area(self):
        return sum(shape.area() for shape in self)

    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self)

    def largest(self):
        if not self:
            return None
        return max(self, key=lambda shape: shape.area())

    def sorted_by_area(self, reverse=False):
        return ShapeList(sorted(self, key=lambda s: s.area(),
                                reverse=reverse))

    def of_type(self, shape_class):
        return ShapeList(s for s in self if isinstance(s, shape_class))
