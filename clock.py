import raytracer.base as rt
import math

HOUR_ROTATION = math.pi / 6
CANVAS_SIZE = 80
RADIUS = 30

twelve = rt.Point(0, 0, 1)
c = rt.Canvas(80, 80)
color = rt.Color(1, 1, 1)

# start at 12 and compute the other 11 hour points
for hour in range(0, 12):
    p = rt.RotationY(hour * HOUR_ROTATION) * twelve
    x = int(p.x * RADIUS) + 40
    y = int(p.z * RADIUS) + 40
    print(f"{hour}: {x},{y}")
    c.write_pixel(x, y, color)

with open("clock.ppm", "w") as ppm_file:
    ppm_file.write(c.to_ppm())
