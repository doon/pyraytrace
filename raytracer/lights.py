from raytracer.base import Point, Color


class PointLight:
    def __init__(self, position: Point, intensity: Color):
        self.position = position
        self.intensity = intensity

    def __eq__(self, other):
        return self.position == other.position and self.intensity == other.intensity

    def __str__(self):
        return (
            f"PointLight:\nPosition: {self.position}\nIntesity: {self.intensity}"
        )
