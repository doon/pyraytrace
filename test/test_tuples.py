import unittest
import math
import raytracer.base as rt


class TestTuples(unittest.TestCase):
    def test_points(self):
        self.assertEqual(rt.Tuple(1.0, 2.0, 3.0, 1.0), rt.Point(1.0, 2.0, 3.0))
        self.assertEqual(rt.Tuple(-1, -1, -1, 1.0), rt.Point(-1, -1, -1))

    def test_vectors(self):
        self.assertEqual(rt.Tuple(1.0, 2.0, 3.0, 0.0), rt.Vector(1.0, 2.0, 3.0))
        self.assertEqual(rt.Tuple(-1, -1, -1, 0.0), rt.Vector(-1, -1, -1))

    def test_addition(self):
        a = rt.Tuple(3, -2, 5, 1)
        b = rt.Tuple(-2, 3, 1, 0)
        expected = rt.Tuple(1, 1, 6, 1)
        self.assertEqual(a + b, expected)

    def test_subtraction(self):
        # subtract 2 points gives us a vector
        a = rt.Point(3, 2, 1)
        b = rt.Point(5, 6, 7)
        expected = rt.Vector(-2, -4, -6)
        self.assertEqual(a - b, expected)

        # subtract vector from point gives us a point
        v = rt.Vector(5, 6, 7)
        expected = rt.Point(-2, -4, -6)
        self.assertEqual(a - v, expected)

        # subtract 2 vectors, gives us a vector
        v1 = rt.Vector(3, 2, 1)
        v2 = rt.Vector(5, 6, 7)
        expected = rt.Vector(-2, -4, -6)
        self.assertEqual(v1 - v2, expected)

    def test_negation(self):
        a = rt.Tuple(1, -2, 3, -4)
        expected = rt.Tuple(-1, 2, -3, 4)
        self.assertEqual(-a, expected)

    def test_multiplication(self):
        a = rt.Tuple(1, -2, 3, -4)
        expected = rt.Tuple(3.5, -7, 10.5, -14)
        self.assertEqual(a * 3.5, expected)
        expected1 = rt.Tuple(0.5, -1, 1.5, -2)
        self.assertEqual(a * 0.5, expected1)

    def test_division(self):
        a = rt.Tuple(1, -2, 3, -4)
        expected = rt.Tuple(0.5, -1, 1.5, -2)
        self.assertEqual(a / 2, expected)

    def test_magnitude(self):
        v1 = rt.Vector(1, 0, 0)
        v2 = rt.Vector(0, 1, 0)
        v3 = rt.Vector(0, 0, 1)
        self.assertEqual(v1.magnitude(), 1)
        self.assertEqual(v2.magnitude(), 1)
        self.assertEqual(v3.magnitude(), 1)

        v4 = rt.Vector(1, 2, 3)
        self.assertEqual(v4.magnitude(), math.sqrt(14))

        v5 = rt.Vector(-1, -2, -3)
        self.assertEqual(v5.magnitude(), math.sqrt(14))

    def test_normalize(self):
        v1 = rt.Vector(4, 0, 0)
        expected1 = rt.Vector(1, 0, 0)
        self.assertEqual(v1.normalize(), expected1)
        v2 = rt.Vector(1, 2, 3)
        expected2 = rt.Vector(0.26726, 0.53452, 0.80178)
        self.assertEqual(v2.normalize(), expected2)
        self.assertEqual(v2.normalize().magnitude(), 1)

    def test_dotproduct(self):
        v1 = rt.Vector(1, 2, 3)
        v2 = rt.Vector(2, 3, 4)
        self.assertEqual(v1.dot(v2), 20)

    def test_crossproduct(self):
        v1 = rt.Vector(1, 2, 3)
        v2 = rt.Vector(2, 3, 4)
        self.assertEqual(v1.cross(v2), rt.Vector(-1, 2, -1))
        self.assertEqual(v2.cross(v1), rt.Vector(1, -2, 1))
