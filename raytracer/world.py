from raytracer.lights import PointLight
from raytracer.spheres import Sphere
from raytracer.materials import Material
import raytracer.base as rt
import raytracer.rays as rays


class World:
    def __init__(self):
        self.light = None
        self.objects = []

    @classmethod
    def default(cls):
        world = cls()
        world.light = PointLight(rt.Point(-10, 10, -10), rt.Color(1, 1, 1))
        s1 = Sphere()
        m = Material(color=rt.Color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
        s1.set_material(m)
        s2 = Sphere()
        s2.set_transform(rt.Scaling(0.5, 0.5, 0.5))
        world.objects.append(s1)
        world.objects.append(s2)
        return world

    def intersect(self, ray: rays.Ray):
        xs = []
        for obj in self.objects:
            xs.extend(ray.intersects(obj))
        return sorted(xs)

    def shade_hit(self, comps: rays.Comps):
        return comps.object.material.lighting(
            comps.eyev, comps.normalv, comps.point, self.light
        )
