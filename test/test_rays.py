import unittest
from raytracer.base import *
from raytracer.rays import *
from raytracer.shapes import *


class TestRays(unittest.TestCase):
    def test_creation(self):
        o = Point(1, 2, 3)
        d = Vector(4, 5, 6)
        r = Ray(o, d)
        self.assertEqual(r.origin, o)
        self.assertEqual(r.direction, d)

    def test_position(self):
        r = Ray(Point(2, 3, 4), Vector(1, 0, 0))
        self.assertEqual(r.position(0), Point(2, 3, 4))
        self.assertEqual(r.position(1), Point(3, 3, 4))
        self.assertEqual(r.position(-1), Point(1, 3, 4))
        self.assertEqual(r.position(2.5), Point(4.5, 3, 4))

    def test_intersection(self):
        s = Sphere()
        i = Intersection(3.5, s)
        self.assertEqual(i.object, s)
        self.assertEqual(i.t, 3.5)

    def test_aggregating_intersections(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i1, i2)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[1].t, 2)

    def test_intersects_object(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersects(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].object, s)
        self.assertEqual(xs[1].object, s)

    def test_hit_when_all_positive(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i2, i1)
        h = xs.hit()
        self.assertEqual(h, i1)

    def test_hit_when_some_negative(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i2, i1)
        h = xs.hit()
        self.assertEqual(h, i2)

    def test_hit_when_all_negative(self):
        s = Sphere()
        i1 = Intersection(-2, s)
        i2 = Intersection(-1, s)
        xs = Intersections(i2, i1)
        h = xs.hit()
        self.assertIsNone(h)

    def test_hit_is_lowest_non_negative_intersection(self):
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = Intersections(i1, i2, i3, i4)
        h = xs.hit()
        self.assertEqual(h, i4)

    def test_translate_ray(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        m = Translation(3, 4, 5)
        r2 = r.transform(m)
        self.assertEqual(r2.origin, Point(4, 6, 8))
        self.assertEqual(r2.direction, Vector(0, 1, 0))

    def test_scale_ray(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        m = Scaling(2, 3, 4)
        r2 = r.transform(m)
        self.assertEqual(r2.origin, Point(2, 6, 12))
        self.assertEqual(r2.direction, Vector(0, 3, 0))

    def test_precomputing_state_of_intersection(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        shape = Sphere()
        i = Intersection(4, shape)
        comps = i.prepare_computations(r)
        self.assertEqual(comps.t, i.t)
        self.assertEqual(comps.object, i.object)
        self.assertEqual(comps.point, Point(0, 0, -1))
        self.assertEqual(comps.eyev, Vector(0, 0, -1))
        self.assertEqual(comps.normalv, Vector(0, 0, -1))

    def test_hit_when_intersection_outside(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        shape = Sphere()
        i = Intersection(4, shape)
        comps = i.prepare_computations(r)
        self.assertFalse(comps.inside)

    def test_hit_when_intersection_inside(self):
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        shape = Sphere()
        i = Intersection(1, shape)
        comps = i.prepare_computations(r)
        self.assertEqual(comps.point, Point(0, 0, 1))
        self.assertEqual(comps.eyev, Vector(0, 0, -1))
        self.assertEqual(comps.normalv, Vector(0, 0, -1))
        self.assertTrue(comps.inside)

    def test_the_hit_should_offset_the_point(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        shape = Sphere()
        shape.set_transform(Translation(0, 0, 1))
        i = Intersection(5, shape)
        comps = i.prepare_computations(r)
        self.assertLess(comps.over_point.z, -EPSILON / 2)
