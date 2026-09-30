import unittest

from shape_list import ShapeList
from shapes import Circle, Rectangle, Square


class TestShapeList(unittest.TestCase):
    def setUp(self):
        self.shapes = ShapeList([Rectangle(1, 2), Square(3), Rectangle(2, 2)])

    def test_is_list(self):
        self.assertIsInstance(self.shapes, list)
        self.assertEqual(len(self.shapes), 3)

    def test_rejects_not_shapes(self):
        with self.assertRaises(TypeError):
            self.shapes.append(10)
        with self.assertRaises(TypeError):
            self.shapes.insert(0, "круг")
        with self.assertRaises(TypeError):
            self.shapes.extend([Square(1), None])
        with self.assertRaises(TypeError):
            self.shapes[0] = 5
        with self.assertRaises(TypeError):
            self.shapes += [1]
        with self.assertRaises(TypeError):
            ShapeList([1, 2])

    def test_slice_assignment(self):
        self.shapes[0:2] = [Square(1)]
        self.assertEqual(len(self.shapes), 2)

    def test_total_area_and_perimeter(self):
        self.assertEqual(self.shapes.total_area(), 2 + 9 + 4)
        self.assertEqual(self.shapes.total_perimeter(), 6 + 12 + 8)

    def test_largest(self):
        self.assertEqual(self.shapes.largest().area(), 9)
        self.assertIsNone(ShapeList().largest())

    def test_sorted_by_area(self):
        areas = [s.area() for s in self.shapes.sorted_by_area()]
        self.assertEqual(areas, [2, 4, 9])
        self.assertIsInstance(self.shapes.sorted_by_area(), ShapeList)

    def test_of_type(self):
        self.shapes.append(Circle(1))
        self.assertEqual(len(self.shapes.of_type(Square)), 1)
        # квадрат — тоже прямоугольник
        self.assertEqual(len(self.shapes.of_type(Rectangle)), 3)


if __name__ == "__main__":
    unittest.main()
