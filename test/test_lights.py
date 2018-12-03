import unittest
import raytracer.lights as lights
from raytracer.base import Color, Point


class TestLights(unittest.TestCase):
    def test_point_light(self):
        i = Color(1, 1, 1)
        p = Point(0, 0, 0)
        light = lights.PointLight(p, i)
        self.assertEqual(light.position, p)
        self.assertEqual(light.intensity, i)
