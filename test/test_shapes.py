import unittest
from raytracer.base import *
from raytracer.materials import *
from raytracer.shapes import *


class TestShapes(unittest.TestCase):
    def test_default_tranform(self):
        s = Shape()
        self.assertEqual(s.transform, Identity())

    def test_transform(self):
        s = Shape()
        t = Translation(2, 3, 4)
        s.set_transform(t)
        self.assertEqual(s.transform, t)

    def test_shape_has_default_material(self):
        s = Shape()
        m = Material()
        self.assertEqual(s.material, m)

    def test_assign_material_to_shape(self):
        s = Shape()
        m = Material()
        m.ambient = 1
        s.set_material(m)
        self.assertEqual(s.material, m)
