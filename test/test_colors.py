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
        add = c1 + c2
        self.assertEqual(add, rt.Color(1.6, 0.7, 1.0))
        self.assertIsInstance(add, rt.Color)

    def test_subtraction(self):
        c1 = rt.Color(0.9, 0.6, 0.75)
        c2 = rt.Color(0.7, 0.1, 0.25)
        sub = c1 - c2
        self.assertEqual(sub, rt.Color(0.2, 0.5, 0.5))
        self.assertIsInstance(sub, rt.Color)

    def test_scalar_multiplication(self):
        c = rt.Color(0.2, 0.3, 0.4)
        mult = c * 2
        self.assertEqual(mult, rt.Color(0.4, 0.6, 0.8))
        self.assertIsInstance(mult, rt.Color)

    def test_multiply_colors(self):
        c1 = rt.Color(1, 0.2, 0.4)
        c2 = rt.Color(0.9, 1, 0.1)
        combined = c1 * c2
        self.assertEqual(combined, rt.Color(0.9, 0.2, 0.04))
        self.assertIsInstance(combined, rt.Color)
