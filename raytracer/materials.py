import raytracer.base as rt


class Material:
    def __init__(
        self,
        color: rt.Color = rt.Color(1, 1, 1),
        ambient: float = 0.1,
        diffuse: float = 0.9,
        specular: float = 0.9,
        shininess: float = 200,
    ):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
