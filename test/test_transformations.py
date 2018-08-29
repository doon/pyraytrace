import unittest
import raytracer.base as rt


class TestTransformations(unittest.TestCase):
    def test_multiply_translation_matrix(self):
        transform = rt.Translation(5, -3, 2)
        p = rt.Point(-3, 4, 5)
        expected = rt.Point(2, 1, 7)
        self.assertEqual(transform * p, expected)

    def test_multiply_inverse_translation_matrix(self):
        transform = rt.Translation(5, -3, 2)
        inv = transform.inverse()
        p = rt.Point(-3, 4, 5)
        expected = rt.Point(-8, 7, 3)
        self.assertEqual(inv * p, expected)

    def test_translation_on_vectors(self):
        transform = rt.Translation(5, 3, 2)
        v = rt.Vector(-3, 4, 5)
        self.assertEqual(transform * v, v)

    def test_scaling_point(self):
        transform = rt.Scaling(2, 3, 4)
        p = rt.Point(-4, 6, 8)
        expected = rt.Point(-8, 18, 32)
        self.assertEqual(transform * p, expected)

    def test_scaling_vector(self):
        transform = rt.Scaling(2, 3, 4)
        v = rt.Vector(-4, 6, 8)
        expected = rt.Vector(-8, 18, 32)
        self.assertEqual(transform * v, expected)

    def test_multiple_inverse_scaling_matrix(self):
        transform = rt.Scaling(2, 3, 4)
        inv = transform.inverse()
        v = rt.Vector(-4, 6, 8)
        expected = rt.Vector(-2, 2, 2)
        self.assertEqual(inv * v, expected)

    def test_reflection(self):
        transform = rt.Scaling(-1, 1, 1)
        p = rt.Point(2, 3, 4)
        expected = rt.Point(-2, 3, 4)
        self.assertEqual(transform * p, expected)
