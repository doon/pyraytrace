import unittest
from raytracer.base import Color


class TestColors(unittest.TestCase):
    def test_color(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.red, -0.5)
        self.assertEqual(c.green, 0.4)
        self.assertEqual(c.blue, 1.7)

    def test_addition(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        add = c1 + c2
        self.assertEqual(add, Color(1.6, 0.7, 1.0))
        self.assertIsInstance(add, Color)

    def test_subtraction(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        sub = c1 - c2
        self.assertEqual(sub, Color(0.2, 0.5, 0.5))
        self.assertIsInstance(sub, Color)

    def test_scalar_multiplication(self):
        c = Color(0.2, 0.3, 0.4)
        mult = c * 2
        self.assertEqual(mult, Color(0.4, 0.6, 0.8))
        self.assertIsInstance(mult, Color)

    def test_multiply_colors(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        combined = c1 * c2
        self.assertEqual(combined, Color(0.9, 0.2, 0.04))
        self.assertIsInstance(combined, Color)
