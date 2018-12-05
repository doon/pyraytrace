import unittest
import raytracer.base as rt
import raytracer.rays as ray
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
        light = PointLight(rt.Point(-10, 10, 10), rt.Color(1, 1, 1))
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
        r = ray.Ray(rt.Point(0, 0, -5), rt.Vector(0, 0, 1))
        xs = world.intersect(r)
        self.assertEqual(len(xs), 4)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 4.5)
        self.assertEqual(xs[2].t, 5.5)
        self.assertEqual(xs[3].t, 6)
