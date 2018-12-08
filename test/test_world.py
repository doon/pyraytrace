import unittest
import raytracer.base as rt
import raytracer.rays as rays
from raytracer.spheres import Sphere
from raytracer.lights import PointLight
from raytracer.materials import Material
from raytracer.world import World


class TestWorlds(unittest.TestCase):
    def test_empty_world(self):
        world = World()
        self.assertIsNone(world.light)
        self.assertEqual(len(world.objects), 0)

    def test_default_world(self):
        light = PointLight(rt.Point(-10, 10, -10), rt.Color(1, 1, 1))
        s1 = Sphere()
        m = Material(color=rt.Color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
        s1.set_material(m)
        s2 = Sphere()
        s2.set_transform(rt.Scaling(0.5, 0.5, 0.5))
        world = World.default()
        self.assertEqual(world.light, light)
        self.assertIn(s1, world.objects)
        self.assertIn(s2, world.objects)

    def test_intersect_world_with_ray(self):
        world = World.default()
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        xs = world.intersect(r)
        self.assertEqual(len(xs), 4)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 4.5)
        self.assertEqual(xs[2].t, 5.5)
        self.assertEqual(xs[3].t, 6)

    def test_shading_intersection(self):
        w = World.default()
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        shape = w.objects[0]
        i = rays.Intersection(4, shape)
        comps = i.prepare_computations(r)
        c = w.shade_hit(comps)
        self.assertEqual(c, rt.Color(0.38066, 0.47583, 0.2855))

    def test_shading_intersection_from_inside(self):
        w = World.default()
        w.light = PointLight(rt.Point(0, 0.25, 0), rt.Color(1, 1, 1))
        r = rays.Ray(rt.Point(0, 0, 0), rt.Vector(0, 0, 1))
        shape = w.objects[1]
        i = rays.Intersection(0.5, shape)
        comps = i.prepare_computations(r)
        c = w.shade_hit(comps)
        self.assertEqual(c, rt.Color(0.90498, 0.90498, 0.90498))

    def test_color_at_when_ray_misses(self):
        w = World.default()
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 1, 0))
        c = w.color_at(r)
        self.assertEqual(c, rt.Color(0, 0, 0))

    def test_color_at_when_ray_hits(self):
        w = World.default()
        r = rays.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        c = w.color_at(r)
        self.assertEqual(c, rt.Color(0.38066, 0.47583, 0.2855))

    def test_color_at_with_intersection_behind_the_ray(self):
        w = World.default()
        outer = w.objects[0]
        outer.material.ambient = 1
        inner = w.objects[1]
        inner.material.ambient = 1
        r = rays.Ray(rt.Point(0, 0, 0.75), rt.Vector(0, 0, -1))
        c = w.color_at(r)
        self.assertEqual(c, inner.material.color)

    def test_no_shadow_when_nothing_is_colinear(self):
        w = World.default()
        p = rt.Point(0, 10, 10)
        self.assertFalse(w.shadowed(p))

    def test_shadow_with_between_point_light(self):
        w = World.default()
        p = rt.Point(10, -10, 10)
        self.assertTrue(w.shadowed(p))

    def test_no_shadow_when_object_behind_light(self):
        w = World.default()
        p = rt.Point(-20, 20, -20)
        self.assertFalse(w.shadowed(p))

    def test_no_shadow_when_object_behind_point(self):
        w = World.default()
        p = rt.Point(-2, 2, -2)
        self.assertFalse(w.shadowed(p))
