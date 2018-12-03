import unittest
import raytracer.base as rt
import raytracer.rays as rays
import math


class TestSpheres(unittest.TestCase):
    def test_default_tranform(self):
        s = rt.Sphere()
        self.assertEqual(s.transform, rt.Identity())

    def test_transform(self):
        s = rt.Sphere()
        t = rt.Translation(2, 3, 4)
        s.set_transform(t)
        self.assertEqual(s.transform, t)

    def test_intersecting_scaled_sphere(self):
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        s = rt.Sphere()
        s.set_transform(rt.Scaling(2, 2, 2))
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 3)
        self.assertEqual(xs[1].t, 7)

    def test_intersecting_translated_sphere(self):
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        s = rt.Sphere()
        s.set_transform(rt.Translation(5, 0, 0))
        xs = r.intersects(s)
        self.assertEqual(len(xs), 0)

    def test_normal_at_point_on_x_axis(self):
        s = rt.Sphere()
        n = s.normal_at(rt.Point(1, 0, 0))
        self.assertEqual(n, rt.Vector(1, 0, 0))

    def test_normal_at_point_on_y_axis(self):
        s = rt.Sphere()
        n = s.normal_at(rt.Point(0, 1, 0))
        self.assertEqual(n, rt.Vector(0, 1, 0))

    def test_normal_at_point_on_z_axis(self):
        s = rt.Sphere()
        n = s.normal_at(rt.Point(0, 0, 1))
        self.assertEqual(n, rt.Vector(0, 0, 1))

    def test_normal_at_point_not_on_axis(self):
        s = rt.Sphere()
        n = s.normal_at(rt.Point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))
        self.assertEqual(
            n, rt.Vector(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3)
        )

    def test_normal_is_normalized(self):
        s = rt.Sphere()
        n = s.normal_at(rt.Point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))
        self.assertEqual(n, n.normalize())

    def test_normal_on_translated_sphere(self):
        s = rt.Sphere()
        s.set_transform(rt.Translation(0, 1, 0))
        n = s.normal_at(rt.Point(0, 1.70711, -0.70711))
        self.assertEqual(n, rt.Vector(0, 0.70711, -0.70711))

    def test_normal_on_transformed_sphere(self):
        s = rt.Sphere()
        s.set_transform(rt.Scaling(1, 0.5, 1))
        s.set_transform(rt.RotationZ(math.pi / 5))
        n = s.normal_at(rt.Point(0, math.sqrt(2) / 2, math.sqrt(2) / -2))
        self.assertEqual(n, rt.Vector(0, 0.97014, -0.24254))

