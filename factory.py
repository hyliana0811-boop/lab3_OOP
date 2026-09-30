"""Повышенная сложность №2. Паттерн Factory для создания фигур.

Код, которому нужна фигура, не знает о конкретных классах: он передаёт
фабрике название и параметры. Новые фигуры добавляются регистрацией,
без изменения метода create.
"""

from shapes import Circle, Rectangle, Square, Triangle


class ShapeFactory:
    _registry = {}

    @classmethod
    def register(cls, kind, shape_class):
        cls._registry[kind.lower()] = shape_class

    @classmethod
    def available(cls):
        return sorted(cls._registry)

    @classmethod
    def create(cls, kind, *params):
        shape_class = cls._registry.get(kind.lower())
        if shape_class is None:
            raise ValueError(
                f"Неизвестная фигура {kind!r}. "
                f"Доступны: {', '.join(cls.available())}"
            )
        return shape_class(*params)

    @classmethod
    def from_string(cls, line):
        """Создать фигуру из строки вида 'rectangle 3 4'."""
        parts = line.split()
        if not parts:
            raise ValueError("Пустое описание фигуры")
        params = [float(value) for value in parts[1:]]
        return cls.create(parts[0], *params)


ShapeFactory.register("circle", Circle)
ShapeFactory.register("rectangle", Rectangle)
ShapeFactory.register("square", Square)
ShapeFactory.register("triangle", Triangle)
