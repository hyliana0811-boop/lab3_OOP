import math
import unittest

from shapes import Circle, Rectangle, Shape, Square, Triangle


class TestShapes(unittest.TestCase):
    def test_circle(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), 4 * math.pi)
        self.assertAlmostEqual(circle.perimeter(), 4 * math.pi)

    def test_rectangle(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)
        self.assertEqual(rect.perimeter(), 14)

    def test_square_is_rectangle(self):
        square = Square(5)
        self.assertIsInstance(square, Rectangle)
        self.assertEqual(square.area(), 25)
        self.assertEqual(square.perimeter(), 20)

    def test_triangle_heron(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)
        self.assertEqual(triangle.perimeter(), 12)

    def test_impossible_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_negative_sizes(self):
        for make in (lambda: Circle(-1), lambda: Rectangle(0, 2),
                     lambda: Square(-3)):
            with self.assertRaises(ValueError):
                make()

    def test_base_class_is_abstract_by_convention(self):
        with self.assertRaises(NotImplementedError):
            Shape().area()

    def test_polymorphism(self):
        shapes = [Circle(1), Rectangle(1, 2), Triangle(3, 4, 5)]
        names = [shape.describe().split(":")[0] for shape in shapes]
        self.assertEqual(names, ["круг", "прямоугольник", "треугольник"])
        self.assertEqual(Rectangle(2, 3).describe(),
                         "прямоугольник: площадь 6.00, периметр 10.00")


if __name__ == "__main__":
    unittest.main()
