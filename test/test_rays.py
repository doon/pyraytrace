import unittest
import raytracer.base as rt
import raytracer.rays as rays
from raytracer.spheres import Sphere


class TestRays(unittest.TestCase):
    def test_creation(self):
        o = rt.Point(1, 2, 3)
        d = rt.Vector(4, 5, 6)
        r = rays.Ray(o, d)
        self.assertEqual(r.origin, o)
        self.assertEqual(r.direction, d)

    def test_position(self):
        r = rays.Ray(rt.Point(2, 3, 4), rt.Vector(1, 0, 0))
        self.assertEqual(r.position(0), rt.Point(2, 3, 4))
        self.assertEqual(r.position(1), rt.Point(3, 3, 4))
        self.assertEqual(r.position(-1), rt.Point(1, 3, 4))
        self.assertEqual(r.position(2.5), rt.Point(4.5, 3, 4))

    def test_intersects_sphere(self):
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 6)

    def test_intersects_sphere_at_tangent(self):
        r = rays.Ray(rt.Point(0, 1, -5), rt.Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 5)
        self.assertEqual(xs[1].t, 5)

    def test_misses_sphere(self):
        r = rays.Ray(rt.Point(0, 2, -5), rt.Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 0)

    def test_originates_inside_sphere(self):
        r = rays.Ray(rt.Point(0, 0, 0), rt.Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -1)
        self.assertEqual(xs[1].t, 1)

    def test_spehere_behind_ray(self):
        r = rays.Ray(rt.Point(0, 0, 5), rt.Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -6)
        self.assertEqual(xs[1].t, -4)

    def test_intersection(self):
        s = Sphere()
        i = rays.Intersection(3.5, s)
        self.assertEqual(i.object, s)
        self.assertEqual(i.t, 3.5)

    def test_aggregating_intersections(self):
        s = Sphere()
        i1 = rays.Intersection(1, s)
        i2 = rays.Intersection(2, s)
        xs = rays.Intersections(i1, i2)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[1].t, 2)

    def test_intersects_object(self):
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].object, s)
        self.assertEqual(xs[1].object, s)

    def test_hit_when_all_positive(self):
        s = Sphere()
        i1 = rays.Intersection(1, s)
        i2 = rays.Intersection(2, s)
        xs = rays.Intersections(i2, i1)
        h = xs.hit()
        self.assertEqual(h, i1)

    def test_hit_when_some_negative(self):
        s = Sphere()
        i1 = rays.Intersection(-1, s)
        i2 = rays.Intersection(2, s)
        xs = rays.Intersections(i2, i1)
        h = xs.hit()
        self.assertEqual(h, i2)

    def test_hit_when_all_negative(self):
        s = Sphere()
        i1 = rays.Intersection(-2, s)
        i2 = rays.Intersection(-1, s)
        xs = rays.Intersections(i2, i1)
        h = xs.hit()
        self.assertIsNone(h)

    def test_hit_is_lowest_non_negative_intersection(self):
        s = Sphere()
        i1 = rays.Intersection(5, s)
        i2 = rays.Intersection(7, s)
        i3 = rays.Intersection(-3, s)
        i4 = rays.Intersection(2, s)
        xs = rays.Intersections(i1, i2, i3, i4)
        h = xs.hit()
        self.assertEqual(h, i4)

    def test_translate_ray(self):
        r = rays.Ray(rt.Point(1, 2, 3), rt.Vector(0, 1, 0))
        m = rt.Translation(3, 4, 5)
        r2 = r.transform(m)
        self.assertEqual(r2.origin, rt.Point(4, 6, 8))
        self.assertEqual(r2.direction, rt.Vector(0, 1, 0))

    def test_scale_ray(self):
        r = rays.Ray(rt.Point(1, 2, 3), rt.Vector(0, 1, 0))
        m = rt.Scaling(2, 3, 4)
        r2 = r.transform(m)
        self.assertEqual(r2.origin, rt.Point(2, 6, 12))
        self.assertEqual(r2.direction, rt.Vector(0, 3, 0))

    def test_precomputing_state_of_intersection(self):
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        shape = Sphere()
        i = rays.Intersection(4, shape)
        comps = i.prepare_computations(r)
        self.assertEqual(comps.t, i.t)
        self.assertEqual(comps.object, i.object)
        self.assertEqual(comps.point, rt.Point(0, 0, -1))
        self.assertEqual(comps.eyev, rt.Vector(0, 0, -1))
        self.assertEqual(comps.normalv, rt.Vector(0, 0, -1))

    def test_hit_when_intersection_outside(self):
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        shape = Sphere()
        i = rays.Intersection(4, shape)
        comps = i.prepare_computations(r)
        self.assertFalse(comps.inside)

    def test_hit_when_intersection_inside(self):
        r = rays.Ray(rt.Point(0, 0, 0), rt.Vector(0, 0, 1))
        shape = Sphere()
        i = rays.Intersection(1, shape)
        comps = i.prepare_computations(r)
        self.assertEqual(comps.point, rt.Point(0, 0, 1))
        self.assertEqual(comps.eyev, rt.Vector(0, 0, -1))
        self.assertEqual(comps.normalv, rt.Vector(0, 0, -1))
        self.assertTrue(comps.inside)
