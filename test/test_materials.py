import math
import unittest
from raytracer.base import *
from raytracer.materials import Material
from raytracer.lights import PointLight


class TestMaterials(unittest.TestCase):
    def setUp(self):
        self.m = Material()
        self.pos = Point(0, 0, 0)

    def test_default_material(self):
        self.assertEqual(self.m.color, Color(1, 1, 1))
        self.assertEqual(self.m.ambient, 0.1)
        self.assertEqual(self.m.diffuse, 0.9)
        self.assertEqual(self.m.specular, 0.9)
        self.assertEqual(self.m.shininess, 200)

    def test_light_with_eye_between_light_and_surface(self):
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, Color(1.9, 1.9, 1.9))

    def test_light_with_eye_between_light_and_surface_offest_45d(self):
        eyev = Vector(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, Color(1.0, 1.0, 1.0))

    def test_light_with_eye_opposite_surface_light_offset_45(self):
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, Color(0.7364, 0.7364, 0.7364))

    def test_light_with_eye_in_reflection_vector(self):
        eyev = Vector(0, -math.sqrt(2) / 2, -math.sqrt(2) / 2)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, Color(1.6364, 1.6364, 1.6364))

    def test_light_with_light_behind_surface(self):
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, 10), Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, Color(0.1, 0.1, 0.1))

    def test_lighting_with_surface_in_shadow(self):
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
        inShadow = True
        result = self.m.lighting(eyev, normalv, self.pos, light, inShadow)
        self.assertEqual(result, Color(0.1, 0.1, 0.1))
