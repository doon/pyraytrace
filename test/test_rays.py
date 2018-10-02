import unittest
import raytracer.base as rt
import raytracer.rays as rays


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
        s = rt.Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 6)

    def test_intersects_sphere_at_tangent(self):
        r = rays.Ray(rt.Point(0, 1, -5), rt.Vector(0, 0, 1))
        s = rt.Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 5)
        self.assertEqual(xs[1].t, 5)

    def test_misses_sphere(self):
        r = rays.Ray(rt.Point(0, 2, -5), rt.Vector(0, 0, 1))
        s = rt.Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 0)

    def test_originates_inside_sphere(self):
        r = rays.Ray(rt.Point(0, 0, 0), rt.Vector(0, 0, 1))
        s = rt.Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -1)
        self.assertEqual(xs[1].t, 1)

    def test_spehere_behind_ray(self):
        r = rays.Ray(rt.Point(0, 0, 5), rt.Vector(0, 0, 1))
        s = rt.Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -6)
        self.assertEqual(xs[1].t, -4)

    def test_intersection(self):
        s = rt.Sphere()
        i = rays.Intersection(3.5, s)
        self.assertEqual(i.object, s)
        self.assertEqual(i.t, 3.5)

    def test_aggregating_intersections(self):
        s = rt.Sphere()
        i1 = rays.Intersection(1, s)
        i2 = rays.Intersection(2, s)
        xs = rays.Intersections(i1, i2)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[1].t, 2)

    def test_intersects_object(self):
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        s = rt.Sphere()
        xs = r.intersects(s)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].object, s)
        self.assertEqual(xs[1].object, s)

    def test_hit_when_all_positive(self):
        s = rt.Sphere()
        i1 = rays.Intersection(1, s)
        i2 = rays.Intersection(2, s)
        xs = rays.Intersections(i2, i1)
        h = xs.hit()
        self.assertEqual(h, i1)

    def test_hit_when_some_negative(self):
        s = rt.Sphere()
        i1 = rays.Intersection(-1, s)
        i2 = rays.Intersection(2, s)
        xs = rays.Intersections(i2, i1)
        h = xs.hit()
        self.assertEqual(h, i2)

    def test_hit_when_all_negative(self):
        s = rt.Sphere()
        i1 = rays.Intersection(-2, s)
        i2 = rays.Intersection(-1, s)
        xs = rays.Intersections(i2, i1)
        h = xs.hit()
        self.assertIsNone(h)

    def test_hit_is_lowest_non_negative_intersection(self):
        s = rt.Sphere()
        i1 = rays.Intersection(5, s)
        i2 = rays.Intersection(7, s)
        i3 = rays.Intersection(-3, s)
        i4 = rays.Intersection(2, s)
        xs = rays.Intersections(i1, i2, i3, i4)
        h = xs.hit()
        self.assertEqual(h, i4)
