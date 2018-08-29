import unittest
import math
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

    def test_rotate_point_x(self):
        p = rt.Point(0, 1, 0)
        half_quarter = rt.RotationX(math.pi / 4)
        full_quarter = rt.RotationX(math.pi / 2)
        expected_half = rt.Point(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
        expected_full = rt.Point(0, 0, 1)
        self.assertEqual(half_quarter * p, expected_half)
        self.assertEqual(full_quarter * p, expected_full)

    def test_inverse_rotate_point_x(self):
        p = rt.Point(0, 1, 0)
        half_quarter = rt.RotationX(math.pi / 4)
        inv = half_quarter.inverse()
        expected = rt.Point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)
        self.assertEqual(inv * p, expected)

    def test_rotate_point_y(self):
        p = rt.Point(0, 0, 1)
        half_quarter = rt.RotationY(math.pi / 4)
        full_quarter = rt.RotationY(math.pi / 2)
        expected_half = rt.Point(math.sqrt(2) / 2, 0, math.sqrt(2) / 2)
        expected_full = rt.Point(1, 0, 0)
        self.assertEqual(half_quarter * p, expected_half)
        self.assertEqual(full_quarter * p, expected_full)

    def test_rotate_point_z(self):
        p = rt.Point(0, 1, 0)
        half_quarter = rt.RotationZ(math.pi / 4)
        full_quarter = rt.RotationZ(math.pi / 2)
        expected_half = rt.Point(-math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
        expected_full = rt.Point(-1, 0, 0)
        self.assertEqual(half_quarter * p, expected_half)
        self.assertEqual(full_quarter * p, expected_full)

    def test_shearing_x_to_y(self):
        transform = rt.Shearing(1, 0, 0, 0, 0, 0)
        p = rt.Point(2, 3, 4)
        expected = rt.Point(5, 3, 4)
        self.assertEqual(transform * p, expected)

    def test_shearing_x_to_z(self):
        transform = rt.Shearing(0, 1, 0, 0, 0, 0)
        p = rt.Point(2, 3, 4)
        expected = rt.Point(6, 3, 4)
        self.assertEqual(transform * p, expected)

    def test_shearing_y_to_x(self):
        transform = rt.Shearing(0, 0, 1, 0, 0, 0)
        p = rt.Point(2, 3, 4)
        expected = rt.Point(2, 5, 4)
        self.assertEqual(transform * p, expected)

    def test_shearing_y_to_z(self):
        transform = rt.Shearing(0, 0, 0, 1, 0, 0)
        p = rt.Point(2, 3, 4)
        expected = rt.Point(2, 7, 4)
        self.assertEqual(transform * p, expected)

    def test_shearing_z_to_x(self):
        transform = rt.Shearing(0, 0, 0, 0, 1, 0)
        p = rt.Point(2, 3, 4)
        expected = rt.Point(2, 3, 6)
        self.assertEqual(transform * p, expected)

    def test_shearing_z_to_y(self):
        transform = rt.Shearing(0, 0, 0, 0, 0, 1)
        p = rt.Point(2, 3, 4)
        expected = rt.Point(2, 3, 7)
        self.assertEqual(transform * p, expected)
