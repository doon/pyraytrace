import unittest
from raytracer.base import *
from raytracer.rays import *
from raytracer.shapes import Plane


class TestPlanes(unittest.TestCase):
    def test_normal_of_plane_is_constant(self):
        p = Plane()
        n1 = p.object_normal(Point(0, 0, 0))
        n2 = p.object_normal(Point(10, 0, -10))
        n3 = p.object_normal(Point(-5, 0, 150))
        self.assertEqual(n1, Vector(0, 1, 0))
        self.assertEqual(n2, Vector(0, 1, 0))
        self.assertEqual(n3, Vector(0, 1, 0))

    def test_intersect_with_ray_parallel(self):
        p = Plane()
        r = Ray(Point(0, 10, 0), Vector(0, 0, 1))
        xs = p.local_intersect(r)
        self.assertEqual(len(xs), 0)

    def test_intersect_with_coplanar(self):
        p = Plane()
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        xs = p.local_intersect(r)
        self.assertEqual(len(xs), 0)

    def test_intersect_from_above(self):
        p = Plane()
        r = Ray(Point(0, 1, 0), Vector(0, -1, 0))
        xs = p.local_intersect(r)
        self.assertEqual(len(xs), 1)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[0].object, p)

    def test_intersect_from_above(self):
        p = Plane()
        r = Ray(Point(0, -1, 0), Vector(0, 1, 0))
        xs = p.local_intersect(r)
        self.assertEqual(len(xs), 1)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[0].object, p)
