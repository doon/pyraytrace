import unittest
import raytracer.base as rt
import raytracer.rays as rays


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
        r = rays.Ray(rt.Point(0,0,-5), rt.Vector(0,0,1))
        s = rt.Sphere()
        s.set_transform(rt.Translation(5,0,0))
        xs = r.intersects(s)
        self.assertEqual(len(xs),0)
