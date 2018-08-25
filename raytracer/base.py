import math

EPSILON = 0.00001


def equal(a: float, b: float) -> bool:
    if abs(a - b) < EPSILON:
        return True
    return False


class Tuple:
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        return Tuple(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __sub__(self, other):
        return Tuple(
            self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w
        )

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        return Tuple(self.x * other, self.y * other, self.z * other, self.w * other)

    def __truediv__(self, other):
        return Tuple(self.x / other, self.y / other, self.z / other, self.w / other)

    def __eq__(self, other):
        return (
            equal(self.x, other.x)
            and equal(self.y, other.y)
            and equal(self.z, other.z)
            and equal(self.w, other.w)
        )

    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)

    def __str__(self) -> str:
        return f"x: {self.x} , y: {self.y}, z: {self.z}, w: {self.w}"


class Point(Tuple):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0)

    def __str__(self) -> str:
        return f"Point: < {self.x}, {self.y}, {self.z}>"


class Vector(Tuple):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 0.0)

    def __str__(self) -> str:
        return f"Vector: < {self.x}, {self.y}, {self.z}>"

    def normalize(self):
        m = self.magnitude()
        return Tuple(self.x / m, self.y / m, self.z / m, self.w / m)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w + other.w

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )


class Color(Tuple):
    def __init__(self, r: float, g: float, b: float):
        super().__init__(r, g, b, 0.0)

    @property
    def red(self):
        return self.x

    @property
    def green(self):
        return self.y

    @property
    def blue(self):
        return self.z

    def __mul__(self, other):
        if isinstance(other, Color):
            r = self.red * other.red
            g = self.green * other.green
            b = self.blue * other.blue
            return Color(r, g, b)
        else:
            r = self.red * other
            g = self.green * other
            b = self.blue * other
            return Color(r, g, b)
