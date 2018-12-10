import math
from raytracer.base import *
from raytracer.shapes import *
from raytracer.world import World
from raytracer.lights import PointLight
from raytracer.camera import Camera

world = World()

floor = Plane()
floor.material.color = Color(1, 0.9, 0.9)
floor.material.specular = 0

world.objects.append(floor)

middle = Sphere()
middle.set_transform(Translation(-0.5, 1, 0.5))
middle.material.color = Color(0.1, 1, 0.5)
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = Sphere()
right.set_transform(Translation(1.5, 0.5, -0.5))
right.set_transform(Scaling(0.5, 0.5, 0.5))
right.material.color = Color(0.5, 1, 0.1)
right.material.diffuse = 0.7
right.material.specular = 0.3

left = Sphere()
left.set_transform(Translation(-1.5, 0.33, -0.75))
left.set_transform(Scaling(0.33, 0.33, 0.33))
left.material.color = Color(1, 0.8, 0.1)
left.material.diffuse = 0.7
left.material.specular = 0.3

world.objects.append(middle)
world.objects.append(right)
world.objects.append(left)

world.light = PointLight(Point(-10, 10, -10), Color(1, 1, 1))
camera = Camera(
    200,
    100,
    math.pi / 3,
    ViewTransform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0)),
)

canvas = camera.render(world)
with open("second_scene.ppm", "w") as ppm_file:
    ppm_file.write(canvas.to_ppm())
