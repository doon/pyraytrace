from raytracer.base import *
from raytracer.lights import *
from raytracer.materials import *
from raytracer.rays import *
from raytracer.shapes import *


class World:
    def __init__(self):
        self.light = None
        self.objects = []

    @classmethod
    def default(cls):
        world = cls()
        world.light = PointLight(Point(-10, 10, -10), Color(1, 1, 1))
        s1 = Sphere()
        m = Material(color=Color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
        s1.set_material(m)
        s2 = Sphere()
        s2.set_transform(Scaling(0.5, 0.5, 0.5))
        world.objects.append(s1)
        world.objects.append(s2)
        return world

    def intersect(self, ray: Ray):
        xs = Intersections()
        for obj in self.objects:
            xs.extend(obj.intersects(ray))
        xs.sort()
        return xs

    def shade_hit(self, comps: Comps):
        shadow = self.shadowed(comps.over_point)
        return comps.object.material.lighting(
            comps.eyev, comps.normalv, comps.point, self.light, shadow
        )

    def color_at(self, ray: Ray):
        xs = self.intersect(ray)
        hit = xs.hit()
        if hit is None:
            return Color(0, 0, 0)
        else:
            return self.shade_hit(hit.prepare_computations(ray))

    def shadowed(self, point: Point):
        v = self.light.position - point
        distance = v.magnitude()
        direction = v.normalize()
        r = Ray(point, direction)
        xs = self.intersect(r)
        h = xs.hit()
        if h is not None and h.t < distance:
            return True
        return False

    def __str__(self):
        str = f"world: Light: {self.light}\nObjects:\n"
        for obj in self.objects:
            str = str + f"{obj}\n"
        return str
