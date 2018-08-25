import raytracer.base as rt

from typing import NamedTuple


class World(NamedTuple):
    gravity: rt.Vector
    wind: rt.Vector


class Projectile(NamedTuple):
    position: rt.Point
    velocity: rt.Vector


def tick(world: World, p: Projectile) -> Projectile:
    pos = p.position + p.velocity
    velocity = p.velocity + world.gravity + world.wind
    return Projectile(pos, velocity)


start = rt.Point(0, 1, 0)
vel = rt.Vector(1, 1, 0).normalize() * 4
p = Projectile(start, vel)
w = World(rt.Vector(0, -0.1, 0), rt.Vector(-0.01, 0, 0))

t = 0
while p.position.y > 0:
    print(f"Tick {t}: Position {p.position}")
    p = tick(w, p)
    t = t + 1

print(f"\nTook {t} ticks to hit ground")
