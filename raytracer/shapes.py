from raytracer.base import *
from raytracer.materials import *
from raytracer.rays import *


class Shape:
    def __init__(self):
        self.transform = Identity()
        self.material = Material()

    def set_transform(self, transform: Matrix):
        self.transform *= transform

    def normal_at(self, world_point: Point):
        obj_point = self.transform.inverse() * world_point
        object_normal = self.object_normal(obj_point)
        world_normal = self.transform.inverse().transpose() * object_normal
        world_normal.w = 0
        return world_normal.normalize()

    def intersects(self, ray: Ray):
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    def set_material(self, material: Material):
        self.material = material


class Sphere(Shape):
    def __init__(self):
        self.origin = Point(0, 0, 0)
        self.radius = 1
        super().__init__()

    def object_normal(self, point: Point):
        return point - self.origin

    def local_intersect(self, ray: Ray):
        obj_to_ray = ray.origin - self.origin
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(obj_to_ray)
        c = obj_to_ray.dot(obj_to_ray) - 1

        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return Intersections()

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)

        if t1 > t2:
            return Intersections(Intersection(t2, self), Intersection(t1, self))
        return Intersections(Intersection(t1, self), Intersection(t2, self))

    def __eq__(self, other):
        return (
            isinstance(other, Sphere)
            and self.origin == other.origin
            and self.radius == other.radius
            and self.transform == other.transform
        )

    def __str__(self):
        return f"Sphere:\nOrigin: {self.origin}\nMaterial:{self.material}\nTransform:\n {self.transform}"
