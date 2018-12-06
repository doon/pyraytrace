import raytracer.base as rt
import raytracer.materials as mat


class Sphere:
    def __init__(self):
        self.origin = rt.Point(0, 0, 0)
        self.radius = 1
        self.transform = rt.Identity()
        self.material = mat.Material()

    def __eq__(self, other):
        return (
            self.origin == other.origin
            and self.radius == other.radius
            and self.transform == other.transform
        )

    def set_transform(self, transform: rt.Matrix):
        self.transform *= transform

    def normal_at(self, world_point: rt.Point):
        obj_point = self.transform.inverse() * world_point
        object_normal = obj_point - self.origin
        world_normal = self.transform.inverse().transpose() * object_normal
        world_normal.w = 0
        return world_normal.normalize()

    def set_material(self, material: mat.Material):
        self.material = material
