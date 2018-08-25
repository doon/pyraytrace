from typing import NamedTuple
import math

EPSILON = 0.00001


def equal(a: float, b: float) -> bool:
    if abs(a - b) < EPSILON:
        return True
    return False


class Tup(NamedTuple):
    x: float
    y: float
    z: float
    w: float

    def __add__(self, other):
        return Tup(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __sub__(self, other):
        return Tup(
            self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w
        )

    def __neg__(self):
        return Tup(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        return Tup(self.x * other, self.y * other, self.z * other, self.w * other)

    def __truediv__(self, other):
        return Tup(self.x / other, self.y / other, self.z / other, self.w / other)

    def __eq__(self, other):
        return (
            equal(self.x, other.x)
            and equal(self.y, other.y)
            and equal(self.z, other.z)
            and equal(self.w, other.w)
        )


def point(x: float, y: float, z: float) -> Tup:
    return Tup(x=x, y=y, z=z, w=1.0)


def vector(x: float, y: float, z: float) -> Tup:
    return Tup(x=x, y=y, z=z, w=0.0)


def magnitude(v: Tup) -> float:
    return math.sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2 + v.w ** 2)


def normalize(v: Tup) -> Tup:
    m = magnitude(v)
    return Tup(v.x / m, v.y / m, v.z / m, v.w / m)


def dot(v1: Tup, v2: Tup) -> float:
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z + v1.w + v2.w


def cross(v1: Tup, v2: Tup) -> Tup:
    return vector(
        v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z, v1.x * v2.y - v1.y * v2.x
    )
