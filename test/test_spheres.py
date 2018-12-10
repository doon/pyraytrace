import unittest
import math
from raytracer.base import *
from raytracer.rays import *
from raytracer.materials import *
from raytracer.shapes import *


class TestSpheres(unittest.TestCase):
    def test_sphere_is_a_shape(self):
        s = Sphere()
        self.assertIsInstance(s,Shape)

    def test_intersecting_scaled_sphere(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.set_transform(Scaling(2, 2, 2))
        xs = s.intersects(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 3)
        self.assertEqual(xs[1].t, 7)

    def test_intersecting_translated_sphere(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.set_transform(Translation(5, 0, 0))
        xs = s.intersects(r)
        self.assertEqual(len(xs), 0)

    def test_normal_at_point_on_x_axis(self):
        s = Sphere()
        n = s.normal_at(Point(1, 0, 0))
        self.assertEqual(n, Vector(1, 0, 0))

    def test_normal_at_point_on_y_axis(self):
        s = Sphere()
        n = s.normal_at(Point(0, 1, 0))
        self.assertEqual(n, Vector(0, 1, 0))

    def test_normal_at_point_on_z_axis(self):
        s = Sphere()
        n = s.normal_at(Point(0, 0, 1))
        self.assertEqual(n, Vector(0, 0, 1))

    def test_normal_at_point_not_on_axis(self):
        s = Sphere()
        n = s.normal_at(Point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))
        self.assertEqual(
            n, Vector(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3)
        )

    def test_normal_is_normalized(self):
        s = Sphere()
        n = s.normal_at(Point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))
        self.assertEqual(n, n.normalize())

    def test_normal_on_translated_sphere(self):
        s = Sphere()
        s.set_transform(Translation(0, 1, 0))
        n = s.normal_at(Point(0, 1.70711, -0.70711))
        self.assertEqual(n, Vector(0, 0.70711, -0.70711))

    def test_normal_on_transformed_sphere(self):
        s = Sphere()
        s.set_transform(Scaling(1, 0.5, 1))
        s.set_transform(RotationZ(math.pi / 5))
        n = s.normal_at(Point(0, math.sqrt(2) / 2, math.sqrt(2) / -2))
        self.assertEqual(n, Vector(0, 0.97014, -0.24254))

    def test_intersects_sphere(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersects(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 6)

    def test_intersects_sphere_at_tangent(self):
        r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersects(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 5)
        self.assertEqual(xs[1].t, 5)

    def test_misses_sphere(self):
        r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersects(r)
        self.assertEqual(len(xs), 0)

    def test_originates_inside_sphere(self):
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersects(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -1)
        self.assertEqual(xs[1].t, 1)

    def test_spehere_behind_ray(self):
        r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersects(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -6)
        self.assertEqual(xs[1].t, -4)
