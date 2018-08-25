import unittest
import raytracer.base as rt


class TestColors(unittest.TestCase):
    def test_color(self):
        c = rt.Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.red, -0.5)
        self.assertEqual(c.green, 0.4)
        self.assertEqual(c.blue, 1.7)

    def test_addition(self):
        c1 = rt.Color(0.9, 0.6, 0.75)
        c2 = rt.Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 + c2, rt.Color(1.6, 0.7, 1.0))

    def test_subtraction(self):
        c1 = rt.Color(0.9, 0.6, 0.75)
        c2 = rt.Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 - c2, rt.Color(0.2, 0.5, 0.5))

    def test_scalar_multiplication(self):
        c = rt.Color(0.2, 0.3, 0.4)
        self.assertEqual(c * 2, rt.Color(0.4, 0.6, 0.8))

    def test_multiply_colors(self):
        c1 = rt.Color(1, 0.2, 0.4)
        c2 = rt.Color(0.9, 1, 0.1)
        self.assertEqual(c1 * c2, rt.Color(0.9, 0.2, 0.04))
