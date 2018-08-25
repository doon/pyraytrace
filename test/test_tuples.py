import unittest
import math
import raytracer.base as rt


class TestTuples(unittest.TestCase):
    def test_points(self):
        self.assertEqual(rt.Tup(1.0, 2.0, 3.0, 1.0), rt.point(1.0, 2.0, 3.0))
        self.assertEqual(rt.Tup(-1, -1, -1, 1.0), rt.point(-1, -1, -1))

    def test_vectors(self):
        self.assertEqual(rt.Tup(1.0, 2.0, 3.0, 0.0), rt.vector(1.0, 2.0, 3.0))
        self.assertEqual(rt.Tup(-1, -1, -1, 0.0), rt.vector(-1, -1, -1))

    def test_addition(self):
        a = rt.Tup(3, -2, 5, 1)
        b = rt.Tup(-2, 3, 1, 0)
        expected = rt.Tup(1, 1, 6, 1)
        self.assertEqual(a + b, expected)

    def test_subtraction(self):
        # subtract 2 points gives us a vector
        a = rt.point(3, 2, 1)
        b = rt.point(5, 6, 7)
        expected = rt.vector(-2, -4, -6)
        self.assertEqual(a - b, expected)

        # subtract vector from point gives us a point
        v = rt.vector(5, 6, 7)
        expected = rt.point(-2, -4, -6)
        self.assertEqual(a - v, expected)

        # subtract 2 vectors, gives us a vector
        v1 = rt.vector(3, 2, 1)
        v2 = rt.vector(5, 6, 7)
        expected = rt.vector(-2, -4, -6)
        self.assertEqual(v1 - v2, expected)

    def test_negation(self):
        a = rt.Tup(1, -2, 3, -4)
        expected = rt.Tup(-1, 2, -3, 4)
        self.assertEqual(-a, expected)

    def test_multiplication(self):
        a = rt.Tup(1, -2, 3, -4)
        expected = rt.Tup(3.5, -7, 10.5, -14)
        self.assertEqual(a * 3.5, expected)
        expected1 = rt.Tup(0.5, -1, 1.5, -2)
        self.assertEqual(a * 0.5, expected1)

    def test_division(self):
        a = rt.Tup(1, -2, 3, -4)
        expected = rt.Tup(0.5, -1, 1.5, -2)
        self.assertEqual(a / 2, expected)

    def test_magnitude(self):
        v1 = rt.vector(1, 0, 0)
        v2 = rt.vector(0, 1, 0)
        v3 = rt.vector(0, 0, 1)
        self.assertEqual(rt.magnitude(v1), 1)
        self.assertEqual(rt.magnitude(v2), 1)
        self.assertEqual(rt.magnitude(v3), 1)

        v4 = rt.vector(1, 2, 3)
        self.assertEqual(rt.magnitude(v4), math.sqrt(14))

        v5 = rt.vector(-1, -2, -3)
        self.assertEqual(rt.magnitude(v5), math.sqrt(14))

    def test_normalize(self):
        v1 = rt.vector(4, 0, 0)
        expected1 = rt.vector(1, 0, 0)
        self.assertEqual(rt.normalize(v1), expected1)
        v2 = rt.vector(1, 2, 3)
        expected2 = rt.vector(0.26726, 0.53452, 0.80178)
        self.assertEqual(rt.normalize(v2), expected2)
        self.assertEqual(rt.magnitude(rt.normalize(v2)), 1)

    def test_dotproduct(self):
        v1 = rt.vector(1, 2, 3)
        v2 = rt.vector(2, 3, 4)
        self.assertEqual(rt.dot(v1, v2), 20)

    def test_crossproduct(self):
        v1 = rt.vector(1, 2, 3)
        v2 = rt.vector(2, 3, 4)
        self.assertEqual(rt.cross(v1, v2), rt.vector(-1, 2, -1))
        self.assertEqual(rt.cross(v2, v1), rt.vector(1, -2, 1))
