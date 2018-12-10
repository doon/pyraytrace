import copy
import math


EPSILON = 0.00001


def equal(a: float, b: float) -> bool:
    if abs(a - b) < EPSILON:
        return True
    return False


def clamp(n: float, minn: int, maxn: int) -> int:
    return int(max(min(maxn, n), minn))


class Tuple:
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        return self.__class__(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __sub__(self, other):
        return self.__class__(
            self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w
        )

    def __neg__(self):
        return self.__class__(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        return self.__class__(
            self.x * other, self.y * other, self.z * other, self.w * other
        )

    def __truediv__(self, other):
        return self.__class__(
            self.x / other, self.y / other, self.z / other, self.w / other
        )

    def __eq__(self, other):
        return (
            equal(self.x, other.x)
            and equal(self.y, other.y)
            and equal(self.z, other.z)
            and equal(self.w, other.w)
        )

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)

    def normalize(self):
        m = self.magnitude()
        return self.__class__(self.x / m, self.y / m, self.z / m, self.w / m)

    def reflect(self, normal):
        return self - normal * 2 * self.dot(normal)

    def __str__(self) -> str:
        return f"x: {self.x} , y: {self.y}, z: {self.z}, w: {self.w}"

    def cross(self, other):
        return self.__class__(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )


class Point(Tuple):
    def __init__(self, x: float, y: float, z: float, w: float = 1.0):
        super().__init__(x, y, z, w)

    def __str__(self) -> str:
        return f"Point: < {self.x}, {self.y}, {self.z}>"


class Vector(Tuple):
    def __init__(self, x: float, y: float, z: float, w: float = 0.0):
        super().__init__(x, y, z, w)

    def __str__(self) -> str:
        return f"Vector: < {self.x}, {self.y}, {self.z}>"


class Color(Tuple):
    def __init__(self, r: float, g: float, b: float, w: float = 0.0):
        super().__init__(r, g, b, w)

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

        return super().__mul__(other)

    def to_rgb(self):
        r = clamp(math.ceil(self.red * 255), 0, 255)
        g = clamp(math.ceil(self.green * 255), 0, 255)
        b = clamp(math.ceil(self.blue * 255), 0, 255)
        return (r, g, b)

    def __str__(self):
        return f"Color: R: {self.red} G: {self.green} B: {self.blue}"


class Canvas:
    def __init__(self, width: int, height: int, color: Color = None):
        self.height = height
        self.width = width
        if color is None:
            color = Color(0, 0, 0)
        self.pixels = [[color] * width for i in range(height)]

    def write_pixel(self, x: int, y: int, color: Color):
        self.pixels[y][x] = color

    def pixel_at(self, x: int, y: int):
        return self.pixels[y][x]

    def _build_header(self):
        return f"P3\n{self.width} {self.height}\n255\n"

    def to_ppm(self):
        header = self._build_header()
        pixel_data = ""

        for row in self.pixels:
            ppm_row = []
            for elem in row:
                (r, g, b) = elem.to_rgb()
                ppm_row.extend([r, g, b])
            # break into at most 17 elements per line to stay < 70 chars
            for line in [ppm_row[i : i + 17] for i in range(0, len(ppm_row), 17)]:
                pixel_data = pixel_data + " ".join(str(c) for c in line) + "\n"
        return header + pixel_data


class Matrix:
    def __init__(self, matrix):
        self.size = len(matrix)
        for x in matrix:
            if len(x) != self.size:
                raise TypeError
        self.matrix = matrix

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __mul__(self, other):
        # are we multiplying by another matrix
        if isinstance(other, Matrix):
            m = [([0] * self.size) for _ in range(self.size)]
            for row in range(self.size):
                for col in range(self.size):
                    sum = 0
                    for index in range(self.size):
                        sum += self[row][index] * other[index][col]
                    m[row][col] = sum
            return Matrix(m)
        elif isinstance(other, Tuple):
            # we are multiply by a tuple
            return Tuple(
                Tuple(self[0][0], self[0][1], self[0][2], self[0][3]).dot(other),
                Tuple(self[1][0], self[1][1], self[1][2], self[1][3]).dot(other),
                Tuple(self[2][0], self[2][1], self[2][2], self[2][3]).dot(other),
                Tuple(self[3][0], self[3][1], self[3][2], self[3][3]).dot(other),
            )

    def __eq__(self, other):
        if self.size != other.size:
            return False
        for row in range(self.size):
            for col in range(self.size):
                if not equal(self[row][col], other[row][col]):
                    return False

        return True

    def __str__(self):
        output = ""
        for line in self.matrix:
            output = output + " ".join(str(x) for x in line) + "\n"
        return output

    def transpose(self):
        m = [([0] * self.size) for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                m[col][row] = self[row][col]
        return Matrix(m)

    def determinate(self):
        if self.size == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]

        sum = 0
        for col in range(self.size):
            sum = sum + self[0][col] * self.cofactor(0, col)
        return sum

    def sub(self, row, col):
        tmp = copy.deepcopy(self.matrix)
        del tmp[row]
        for row in tmp:
            del row[col]
        return Matrix(tmp)

    def minor(self, row, col):
        return self.sub(row, col).determinate()

    def cofactor(self, row, col):
        minor = self.minor(row, col)
        if (row + col) % 2 == 1:
            minor = -minor
        return minor

    def invertible(self):
        return self.determinate() != 0

    def inverse(self):
        m = [([0] * self.size) for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                m[row][col] = self.cofactor(row, col)
        co_matrix = Matrix(m)
        co_matrix = co_matrix.transpose()
        det = self.determinate()
        for row in range(co_matrix.size):
            for col in range(co_matrix.size):
                co_matrix[row][col] = co_matrix[row][col] / det
        return co_matrix


class Identity(Matrix):
    def __init__(self):
        super().__init__([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


class Translation(Identity):
    def __init__(self, x, y, z):
        super().__init__()
        self[0][3] = x
        self[1][3] = y
        self[2][3] = z


class Scaling(Identity):
    def __init__(self, x, y, z):
        super().__init__()
        self[0][0] = x
        self[1][1] = y
        self[2][2] = z


class RotationX(Matrix):
    def __init__(self, r):
        super().__init__(
            [
                [1, 0, 0, 0],
                [0, math.cos(r), -math.sin(r), 0],
                [0, math.sin(r), math.cos(r), 0],
                [0, 0, 0, 1],
            ]
        )


class RotationY(Matrix):
    def __init__(self, r):
        super().__init__(
            [
                [math.cos(r), 0, math.sin(r), 0],
                [0, 1, 0, 0],
                [-math.sin(r), 0, math.cos(r), 0],
                [0, 0, 0, 1],
            ]
        )


class RotationZ(Matrix):
    def __init__(self, r):
        super().__init__(
            [
                [math.cos(r), -math.sin(r), 0, 0],
                [math.sin(r), math.cos(r), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )


class Shearing(Matrix):
    def __init__(self, xy, xz, yx, yz, zx, zy):
        super().__init__([[1, xy, xz, 0], [yx, 1, yz, 0], [zx, zy, 1, 0], [0, 0, 0, 1]])

    # class ViewTransform(Matrix):


def ViewTransform(frm: Point, to: Point, up: Vector) -> Matrix:
    forward = (to - frm).normalize()
    upn = up.normalize()
    left = forward.cross(upn)
    true_up = left.cross(forward)
    orientation = Matrix(
        [
            [left.x, left.y, left.z, 0],
            [true_up.x, true_up.y, true_up.z, 0],
            [-forward.x, -forward.y, -forward.z, 0],
            [0, 0, 0, 1],
        ]
    )
    return orientation * Translation(-frm.x, -frm.y, -frm.z)
