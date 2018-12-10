import unittest
import math
from raytracer.base import *


class TestTransformations(unittest.TestCase):
    def test_multiply_translation_matrix(self):
        transform = Translation(5, -3, 2)
        p = Point(-3, 4, 5)
        expected = Point(2, 1, 7)
        self.assertEqual(transform * p, expected)

    def test_multiply_inverse_translation_matrix(self):
        transform = Translation(5, -3, 2)
        inv = transform.inverse()
        p = Point(-3, 4, 5)
        expected = Point(-8, 7, 3)
        self.assertEqual(inv * p, expected)

    def test_translation_on_vectors(self):
        transform = Translation(5, 3, 2)
        v = Vector(-3, 4, 5)
        self.assertEqual(transform * v, v)

    def test_scaling_point(self):
        transform = Scaling(2, 3, 4)
        p = Point(-4, 6, 8)
        expected = Point(-8, 18, 32)
        self.assertEqual(transform * p, expected)

    def test_scaling_vector(self):
        transform = Scaling(2, 3, 4)
        v = Vector(-4, 6, 8)
        expected = Vector(-8, 18, 32)
        self.assertEqual(transform * v, expected)

    def test_multiple_inverse_scaling_matrix(self):
        transform = Scaling(2, 3, 4)
        inv = transform.inverse()
        v = Vector(-4, 6, 8)
        expected = Vector(-2, 2, 2)
        self.assertEqual(inv * v, expected)

    def test_reflection(self):
        transform = Scaling(-1, 1, 1)
        p = Point(2, 3, 4)
        expected = Point(-2, 3, 4)
        self.assertEqual(transform * p, expected)

    def test_rotate_point_x(self):
        p = Point(0, 1, 0)
        half_quarter = RotationX(math.pi / 4)
        full_quarter = RotationX(math.pi / 2)
        expected_half = Point(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
        expected_full = Point(0, 0, 1)
        self.assertEqual(half_quarter * p, expected_half)
        self.assertEqual(full_quarter * p, expected_full)

    def test_inverse_rotate_point_x(self):
        p = Point(0, 1, 0)
        half_quarter = RotationX(math.pi / 4)
        inv = half_quarter.inverse()
        expected = Point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)
        self.assertEqual(inv * p, expected)

    def test_rotate_point_y(self):
        p = Point(0, 0, 1)
        half_quarter = RotationY(math.pi / 4)
        full_quarter = RotationY(math.pi / 2)
        expected_half = Point(math.sqrt(2) / 2, 0, math.sqrt(2) / 2)
        expected_full = Point(1, 0, 0)
        self.assertEqual(half_quarter * p, expected_half)
        self.assertEqual(full_quarter * p, expected_full)

    def test_rotate_point_z(self):
        p = Point(0, 1, 0)
        half_quarter = RotationZ(math.pi / 4)
        full_quarter = RotationZ(math.pi / 2)
        expected_half = Point(-math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
        expected_full = Point(-1, 0, 0)
        self.assertEqual(half_quarter * p, expected_half)
        self.assertEqual(full_quarter * p, expected_full)

    def test_shearing_x_to_y(self):
        transform = Shearing(1, 0, 0, 0, 0, 0)
        p = Point(2, 3, 4)
        expected = Point(5, 3, 4)
        self.assertEqual(transform * p, expected)

    def test_shearing_x_to_z(self):
        transform = Shearing(0, 1, 0, 0, 0, 0)
        p = Point(2, 3, 4)
        expected = Point(6, 3, 4)
        self.assertEqual(transform * p, expected)

    def test_shearing_y_to_x(self):
        transform = Shearing(0, 0, 1, 0, 0, 0)
        p = Point(2, 3, 4)
        expected = Point(2, 5, 4)
        self.assertEqual(transform * p, expected)

    def test_shearing_y_to_z(self):
        transform = Shearing(0, 0, 0, 1, 0, 0)
        p = Point(2, 3, 4)
        expected = Point(2, 7, 4)
        self.assertEqual(transform * p, expected)

    def test_shearing_z_to_x(self):
        transform = Shearing(0, 0, 0, 0, 1, 0)
        p = Point(2, 3, 4)
        expected = Point(2, 3, 6)
        self.assertEqual(transform * p, expected)

    def test_shearing_z_to_y(self):
        transform = Shearing(0, 0, 0, 0, 0, 1)
        p = Point(2, 3, 4)
        expected = Point(2, 3, 7)
        self.assertEqual(transform * p, expected)

    def test_transforms_in_sequence(self):
        p = Point(1, 0, 1)
        a = RotationX(math.pi / 2)
        b = Scaling(5, 5, 5)
        c = Translation(10, 5, 7)
        p2 = a * p
        self.assertEqual(p2, Point(1, -1, 0))
        p3 = b * p2
        self.assertEqual(p3, Point(5, -5, 0))
        p4 = c * p3
        self.assertEqual(p4, Point(15, 0, 7))

    def test_transforms_chained_reverse(self):
        p = Point(1, 0, 1)
        a = RotationX(math.pi / 2)
        b = Scaling(5, 5, 5)
        c = Translation(10, 5, 7)
        t = c * b * a
        self.assertEqual(t * p, Point(15, 0, 7))

    def test_transformation_matrix_for_default_orientation(self):
        frm = Point(0, 0, 0)
        to = Point(0, 0, -1)
        up = Vector(0, 1, 0)
        t = ViewTransform(frm, to, up)
        self.assertEqual(t, Identity())

    def test_view_transformation_matrix_in_positive_z_direction(self):
        frm = Point(0, 0, 0)
        to = Point(0, 0, 1)
        up = Vector(0, 1, 0)
        t = ViewTransform(frm, to, up)
        self.assertEqual(t, Scaling(-1, 1, -1))

    def test_view_transform_moves_the_world(self):
        frm = Point(0, 0, 8)
        to = Point(0, 0, 0)
        up = Vector(0, 1, 0)
        t = ViewTransform(frm, to, up)
        self.assertEqual(t, Translation(0, 0, -8))

    def test_arbitrary_view_transformation(self):
        frm = Point(1, 3, 2)
        to = Point(4, -2, 8)
        up = Vector(1, 1, 0)
        t = ViewTransform(frm, to, up)
        expected = Matrix(
            [
                [-0.50709, 0.50709, 0.67612, -2.36643],
                [0.76772, 0.60609, 0.12122, -2.82843],
                [-0.35857, 0.59761, -0.71714, 0.00000],
                [0.00000, 0.00000, 0.00000, 1.00000],
            ]
        )
        self.assertEqual(t, expected)
