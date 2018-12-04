import math
import unittest
import raytracer.base as rt
from raytracer.materials import Material
from raytracer.lights import PointLight


class TestMaterials(unittest.TestCase):
    def setUp(self):
        self.m = Material()
        self.pos = rt.Point(0, 0, 0)

    def test_default_material(self):
        # m = mat.Material()
        self.assertEqual(self.m.color, rt.Color(1, 1, 1))
        self.assertEqual(self.m.ambient, 0.1)
        self.assertEqual(self.m.diffuse, 0.9)
        self.assertEqual(self.m.specular, 0.9)
        self.assertEqual(self.m.shininess, 200)

    def test_light_with_eye_between_light_and_surface(self):
        eyev = rt.Vector(0, 0, -1)
        normalv = rt.Vector(0, 0, -1)
        light = PointLight(rt.Point(0, 0, -10), rt.Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, rt.Color(1.9, 1.9, 1.9))

    def test_light_with_eye_between_light_and_surface_offest_45d(self):
        eyev = rt.Vector(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
        normalv = rt.Vector(0, 0, -1)
        light = PointLight(rt.Point(0, 0, -10), rt.Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, rt.Color(1.0, 1.0, 1.0))

    def test_light_with_eye_opposite_surface_light_offset_45(self):
        eyev = rt.Vector(0, 0, -1)
        normalv = rt.Vector(0, 0, -1)
        light = PointLight(rt.Point(0, 10, -10), rt.Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, rt.Color(0.7364, 0.7364, 0.7364))

    def test_light_with_eye_in_reflection_vector(self):
        eyev = rt.Vector(0, -math.sqrt(2) / 2, -math.sqrt(2) / 2)
        normalv = rt.Vector(0, 0, -1)
        light = PointLight(rt.Point(0, 10, -10), rt.Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, rt.Color(1.6364, 1.6364, 1.6364))

    def test_light_with_light_behind_surface(self):
        eyev = rt.Vector(0, 0, -1)
        normalv = rt.Vector(0, 0, -1)
        light = PointLight(rt.Point(0, 0, 10), rt.Color(1, 1, 1))
        result = self.m.lighting(eyev, normalv, self.pos, light)
        self.assertEqual(result, rt.Color(0.1, 0.1, 0.1))
