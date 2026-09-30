import unittest

from factory import ShapeFactory
from shapes import Circle, Shape, Square, Triangle


class TestShapeFactory(unittest.TestCase):
    def test_create(self):
        self.assertIsInstance(ShapeFactory.create("circle", 1), Circle)
        self.assertIsInstance(ShapeFactory.create("SQUARE", 2), Square)

    def test_from_string(self):
        triangle = ShapeFactory.from_string("triangle 3 4 5")
        self.assertIsInstance(triangle, Triangle)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_unknown_shape(self):
        with self.assertRaises(ValueError):
            ShapeFactory.create("hexagon", 1)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            ShapeFactory.from_string("   ")

    def test_register_new_shape(self):
        class Point(Shape):
            name = "точка"

            def area(self):
                return 0

            def perimeter(self):
                return 0

        ShapeFactory.register("point", Point)
        self.addCleanup(ShapeFactory._registry.pop, "point")
        self.assertIn("point", ShapeFactory.available())
        self.assertIsInstance(ShapeFactory.create("point"), Point)


if __name__ == "__main__":
    unittest.main()
