import unittest
import raytracer.base as rt
import raytracer.materials as mat


class TestMaterials(unittest.TestCase):
    def test_default_material(self):
        m = mat.Material()
        self.assertEqual(m.color, rt.Color(1, 1, 1))
        self.assertEqual(m.ambient, 0.1)
        self.assertEqual(m.diffuse, 0.9)
        self.assertEqual(m.specular, 0.9)
        self.assertEqual(m.shininess, 200)
