from raytracer.base import *
from raytracer.rays import *
from raytracer.shapes import *
from raytracer.materials import Material
from raytracer.lights import PointLight

WALL_SIZE = 7
CANVAS_SIZE = 100
PIXEL_SIZE = WALL_SIZE / CANVAS_SIZE
HALF = WALL_SIZE / 2

canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
s = Sphere()
m = Material(color=Color(1, 0.2, 1))
s.material = m

light_postion = Point(-10, 5, -10)
light_color = Color(1, 1, 1)
light = PointLight(light_postion, light_color)


ray_origin = Point(0, 0, -5)
wall_z = 10

for y in range(0, CANVAS_SIZE):
    world_y = HALF - PIXEL_SIZE * y
    for x in range(0, CANVAS_SIZE):
        world_x = -HALF + PIXEL_SIZE * x
        position = Point(world_x, world_y, wall_z)
        v = position - ray_origin
        r = Ray(ray_origin, v.normalize())
        xs = s.intersects(r)
        hit = xs.hit()
        if hit:
            point = r.position(hit.t)
            normal = hit.object.normal_at(point)
            eye = r.direction
            c = hit.object.material.lighting(eye, normal, point, light)
            canvas.write_pixel(x, y, c)

with open("sphere_mat.ppm", "w") as ppm_file:
    ppm_file.write(canvas.to_ppm())
