import math
import unittest
import raytracer.base as rt
from raytracer.camera import Camera
from raytracer.world import World


class TestCamera(unittest.TestCase):
    def test_camera_construction(self):
        hsize = 160
        vsize = 120
        fov = math.pi / 2
        c = Camera(hsize, vsize, fov)
        self.assertEqual(c.hsize, 160)
        self.assertEqual(c.vsize, 120)
        self.assertEqual(c.fov, math.pi / 2)
        self.assertEqual(c.transform, rt.Identity())

    def test_horizontal_pixel_size(self):
        c = Camera(200, 125, math.pi / 2)
        self.assertTrue(rt.equal(c.pixel_size, 0.01))

    def test_vertical_pixel_size(self):
        c = Camera(125, 200, math.pi / 2)
        self.assertTrue(rt.equal(c.pixel_size, 0.01))

    def test_ray_through_center_of_canvas(self):
        c = Camera(201, 101, math.pi / 2)
        r = c.ray_for_pixel(100, 50)
        self.assertEqual(r.origin, rt.Point(0, 0, 0))
        self.assertEqual(r.direction, rt.Vector(0, 0, -1))

    def test_ray_through_corner_of_canvas(self):
        c = Camera(201, 101, math.pi / 2)
        r = c.ray_for_pixel(0, 0)
        self.assertEqual(r.origin, rt.Point(0, 0, 0))
        self.assertEqual(r.direction, rt.Vector(0.66519, 0.33259, -0.66851))

    def test_ray_when_camera_is_transformed(self):
        transform = rt.RotationY(math.pi / 4) * rt.Translation(0, -2, 5)
        c = Camera(201, 101, math.pi / 2, transform)
        r = c.ray_for_pixel(100, 50)
        self.assertEqual(r.origin, rt.Point(0, 2, -5))
        self.assertEqual(r.direction, rt.Vector(math.sqrt(2) / 2, 0, -math.sqrt(2) / 2))

    def test_rendering_world_with_camera(self):
        w = World.default()
        c = Camera(11, 11, math.pi / 2)
        frm = rt.Point(0, 0, -5)
        to = rt.Point(0, 0, 0)
        up = rt.Vector(0, 1, 0)
        c.transform = rt.ViewTransform(frm, to, up)
        image = c.render(w)
        self.assertEqual(image.pixel_at(5, 5), rt.Color(0.38066, 0.47583, 0.2855))
