import raytracer.base as rt
import math
from typing import NamedTuple, Any


class Ray:
    def __init__(self, origin: rt.Point, direction: rt.Vector):
        self.origin = origin
        self.direction = direction

    def position(self, time: float):
        return self.origin + self.direction * time

    def intersects(self, obj):
        ray = self.transform(obj.transform.inverse())
        obj_to_ray = ray.origin - obj.origin
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(obj_to_ray)
        c = obj_to_ray.dot(obj_to_ray) - 1

        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return Intersections()

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)

        if t1 > t2:
            return Intersections(Intersection(t2, obj), Intersection(t1, obj))
        return Intersections(Intersection(t1, obj), Intersection(t2, obj))

    def transform(self, m: rt.Matrix):
        return Ray(m * self.origin, m * self.direction)

    def __str__(self):
        return f"Ray: Origin: {self.origin}, Direction: {self.direction}"


class Comps(NamedTuple):
    t: float
    object: Any
    point: rt.Point
    eyev: rt.Vector
    normalv: rt.Vector
    inside: bool
    over_point: rt.Point


class Intersection:
    def __init__(self, t: float, object):
        self.object = object
        self.t = t

    def __lt__(self, other):
        return self.t < other.t

    def prepare_computations(self, ray: Ray):
        point = ray.position(self.t)
        normalv = self.object.normal_at(point)
        eyev = -ray.direction
        inside = False

        if normalv.dot(eyev) < 0:
            inside = True
            normalv = -normalv
        over_point = point + (normalv * rt.EPSILON)
        return Comps(
            self.t, self.object, point, -ray.direction, normalv, inside, over_point
        )

    def __str__(self):
        return f"Intersection\nt:{self.t}\nobject: {self.object}"


class Intersections(list):
    def __init__(self, *args):
        super(Intersections, self).__init__(args)

    def hit(self) -> Intersection:
        hit = None
        for i in self:
            if i.t > 0 and (hit is None or i.t < hit.t):
                hit = i
        return hit
