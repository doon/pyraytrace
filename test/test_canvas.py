import unittest
from raytracer.base import Canvas, Color


class TestCanvas(unittest.TestCase):
    def test_creation(self):
        canvas = Canvas(10, 20)
        self.assertEqual(canvas.width, 10)
        self.assertEqual(canvas.height, 20)
        black = Color(0, 0, 0)
        for row in canvas.pixels:
            for elem in row:
                self.assertEqual(elem, black)

    def test_writepixel(self):
        canvas = Canvas(10, 20)
        red = Color(1, 0, 0)
        canvas.write_pixel(2, 3, red)
        self.assertEqual(canvas.pixel_at(2, 3), red)
        self.assertNotEqual(canvas.pixel_at(2, 4), red)

    def test_ppm_headers(self):
        canvas = Canvas(5, 3)
        ppm = canvas.to_ppm()
        header = [s.strip() for s in ppm.splitlines()][0:3]
        expected_header = ["P3", "5 3", "255"]
        self.assertEqual(header, expected_header)

    def test_pixel_data(self):
        canvas = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        canvas.write_pixel(0, 0, c1)
        canvas.write_pixel(2, 1, c2)
        canvas.write_pixel(4, 2, c3)
        ppm = canvas.to_ppm()
        pixel_data = [s.strip() for s in ppm.splitlines()][3:6]
        expected_data = [
            "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255",
        ]
        self.assertEqual(pixel_data, expected_data)

    def test_line_length(self):
        canvas = Canvas(10, 2, Color(1, 0.8, 0.6))
        ppm = canvas.to_ppm()
        pixel_data = [s.strip() for s in ppm.splitlines()][3:7]
        expected_data = [
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
            "153 255 204 153 255 204 153 255 204 153 255 204 153",
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
            "153 255 204 153 255 204 153 255 204 153 255 204 153",
        ]
        self.assertEqual(pixel_data, expected_data)

    def file_terminated_by_new_line(self):
        canvas = Canvas(5, 3)
        ppm = canvas.to_ppm()
        self.assertTrue(ppm.endswith("\n"))
