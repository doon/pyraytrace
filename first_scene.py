import math
import raytracer.base as rt
from raytracer.spheres import Sphere
from raytracer.world import World
from raytracer.lights import PointLight
from raytracer.camera import Camera

world = World()

floor = Sphere()
floor.set_transform(rt.Scaling(10, 0.01, 10))
floor.material.color = rt.Color(1, 0.9, 0.9)
floor.material.specular = 0

world.objects.append(floor)

left_wall = Sphere()
left_wall.set_transform(rt.Translation(0, 0, 5))
left_wall.set_transform(rt.RotationY(-math.pi / 4))
left_wall.set_transform(rt.RotationX(math.pi / 2))
left_wall.set_transform(rt.Scaling(10, 0.01, 10))
left_wall.set_material(floor.material)

world.objects.append(left_wall)

right_wall = Sphere()
right_wall.set_transform(rt.Translation(0, 0, 5))
right_wall.set_transform(rt.RotationY(math.pi / 4))
right_wall.set_transform(rt.RotationX(math.pi / 2))
right_wall.set_transform(rt.Scaling(10, 0.01, 10))
right_wall.set_material(floor.material)

world.objects.append(right_wall)

middle = Sphere()
middle.set_transform(rt.Translation(-0.5, 1, 0.5))
middle.material.color = rt.Color(0.1, 1, 0.5)
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = Sphere()
right.set_transform(rt.Translation(1.5, 0.5, -0.5))
right.set_transform(rt.Scaling(0.5, 0.5, 0.5))
right.material.color = rt.Color(0.5, 1, 0.1)
right.material.diffuse = 0.7
right.material.specular = 0.3

left = Sphere()
left.set_transform(rt.Translation(-1.5, 0.33, -0.75))
left.set_transform(rt.Scaling(0.33, 0.33, 0.33))
left.material.color = rt.Color(1, 0.8, 0.1)
left.material.diffuse = 0.7
left.material.specular = 0.3

world.objects.append(middle)
world.objects.append(right)
world.objects.append(left)

world.light = PointLight(rt.Point(-10, 10, -10), rt.Color(1, 1, 1))
camera = Camera(
    200,
    100,
    math.pi / 3,
    rt.ViewTransform(rt.Point(0, 1.5, -5), rt.Point(0, 1, 0), rt.Vector(0, 1, 0)),
)

canvas = camera.render(world)
with open("first_scene.ppm", "w") as ppm_file:
    ppm_file.write(canvas.to_ppm())
