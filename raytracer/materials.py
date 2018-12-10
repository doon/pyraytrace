from raytracer.base import Color, Point, Vector 
from raytracer.lights import PointLight


class Material:
    def __init__(
        self,
        color: Color = Color(1, 1, 1),
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

    def __eq__(self, other):
        return (
            self.color == other.color
            and self.ambient == other.ambient
            and self.diffuse == other.diffuse
            and self.specular == other.specular
            and self.shininess == other.shininess
        )

    def lighting(
        self,
        eyev: Vector,
        normalv: Vector,
        point: Point,
        light: PointLight,
        inShadow: bool = False,
    ):
        diffuse = Color(0, 0, 0)
        specular = Color(0, 0, 0)
        effective_color = self.color * light.intensity
        ambient = effective_color * self.ambient
        if inShadow:
            return ambient

        lightv = (light.position - point).normalize()
        light_dot_normal = lightv.dot(normalv)
        if light_dot_normal >= 0:
            diffuse = effective_color * self.diffuse * light_dot_normal
            reflectv = -lightv.reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)
            if reflect_dot_eye > 0:
                factor = pow(reflect_dot_eye, self.shininess)
                specular = light.intensity * self.specular * factor

        return ambient + diffuse + specular

    def __str__(self):
        return (
            f"Color: {self.color}\n"
            f"Ambient: {self.ambient}\n"
            f"Diffues: {self.diffuse}\n"
            f"Specular: {self.specular}\n"
            f"Shininess: {self.shininess}\n"
        )
