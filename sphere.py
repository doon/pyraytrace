import raytracer.base as rt
import raytracer.rays as rays


WALL_SIZE = 7
CANVAS_SIZE = 100
PIXEL_SIZE = WALL_SIZE / CANVAS_SIZE
HALF = WALL_SIZE / 2

canvas = rt.Canvas(CANVAS_SIZE,CANVAS_SIZE)
c = rt.Color(1,0,0)
s = rt.Sphere()
ray_origin = rt.Point(0,0,-5)
wall_z = 10

for y in range(0, CANVAS_SIZE):
    world_y = HALF - PIXEL_SIZE * y
    for x in range(0,CANVAS_SIZE):
        world_x = -HALF + PIXEL_SIZE * x
        position = rt.Point(world_x, world_y, wall_z)
        v = position - ray_origin
        r = rays.Ray(ray_origin, v.normalize())
        xs = r.intersects(s)
        if xs.hit():
            canvas.write_pixel(x,y,c)

with open("sphere.ppm", "w") as ppm_file:
    ppm_file.write(canvas.to_ppm())