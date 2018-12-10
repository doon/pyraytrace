import unittest
import math
from raytracer.base import *
from raytracer.materials import *
from raytracer.shapes import *


class TestShapes(unittest.TestCase):
    def test_default_tranform(self):
        s = Shape()
        self.assertEqual(s.transform, Identity())

    def test_transform(self):
        s = TestShape()
        t = Translation(2, 3, 4)
        s.set_transform(t)
        self.assertEqual(s.transform, t)

    def test_shape_has_default_material(self):
        s = TestShape()
        m = Material()
        self.assertEqual(s.material, m)

    def test_assign_material_to_shape(self):
        s = TestShape()
        m = Material()
        m.ambient = 1
        s.set_material(m)
        self.assertEqual(s.material, m)

    def test_intersect_scaled_shape_with_ray(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = TestShape()
        s.set_transform(Scaling(2, 2, 2))
        xs = s.intersects(r)
        s.saved_ray = Ray(Point(0, 0, -2.5), Vector(0, 0, 0.5))

    def test_intersecting_translated_shape_with_ray(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = TestShape()
        s.set_transform(Translation(5, 0, 0))
        xs = s.intersects(r)
        s.saved_ray = Ray(Point(-5, 0, -5), Vector(0, 0, 1))

    def test_computing_normal_on_translated_shape(self):
        s = TestShape()
        s.set_transform(Translation(0, 1, 0))
        n = s.normal_at(Point(0, 1.70711, -0.70711))
        self.assertEqual(n, Vector(0, 0.70711, -0.70711))

    def test_computing_normal_on_transformed_sphere(self):
        s = TestShape()
        s.set_transform(Scaling(1, 0.5, 1))
        s.set_transform(RotationZ(math.pi / 5))
        n = s.normal_at(Point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2))
        self.assertEqual(n, Vector(0, 0.97014, -0.24254))
