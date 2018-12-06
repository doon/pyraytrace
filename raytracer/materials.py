import raytracer.base as rt
from raytracer.lights import PointLight


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

    def __eq__(self, other):
        return (
            self.color == other.color
            and self.ambient == other.ambient
            and self.diffuse == other.diffuse
            and self.specular == other.specular
            and self.shininess == other.shininess
        )

    def lighting(
        self, eyev: rt.Vector, normalv: rt.Vector, point: rt.Point, light: PointLight
    ):
        diffuse = rt.Color(0, 0, 0)
        specular = rt.Color(0, 0, 0)
        effective_color = self.color * light.intensity
        lightv = (light.position - point).normalize()
        ambient = effective_color * self.ambient
        light_dot_normal = lightv.dot(normalv)
        if light_dot_normal >= 0:
            diffuse = effective_color * self.diffuse * light_dot_normal
            reflectv = -lightv.reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)
            if reflect_dot_eye > 0:
                factor = pow(reflect_dot_eye, self.shininess)
                specular = light.intensity * self.specular * factor

        return ambient + diffuse + specular
