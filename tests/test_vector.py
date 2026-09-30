import unittest

from vector import Vector


class TestVector(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Vector(1, 2) + Vector(3, 4), Vector(4, 6))

    def test_add_does_not_change_operands(self):
        a, b = Vector(1, 1), Vector(2, 2)
        a + b
        self.assertEqual(a, Vector(1, 1))
        self.assertEqual(b, Vector(2, 2))

    def test_iadd(self):
        v = Vector(1, 1)
        same = v
        v += Vector(1, 2)
        self.assertEqual(v, Vector(2, 3))
        self.assertIs(v, same)

    def test_sum_of_vectors(self):
        vectors = [Vector(1, 0), Vector(0, 1), Vector(2, 2)]
        self.assertEqual(sum(vectors), Vector(3, 3))

    def test_add_wrong_type(self):
        with self.assertRaises(TypeError):
            Vector(1, 1) + 5

    def test_other_operators(self):
        self.assertEqual(Vector(5, 5) - Vector(2, 1), Vector(3, 4))
        self.assertEqual(Vector(1, 2) * 3, Vector(3, 6))
        self.assertEqual(2 * Vector(1, 2), Vector(2, 4))
        self.assertEqual(abs(Vector(3, 4)), 5)


if __name__ == "__main__":
    unittest.main()
