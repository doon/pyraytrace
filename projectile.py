import raytracer.base

from typing import NamedTuple


class World(NamedTuple):
    gravity: Tup
    wind: Tup


class Projectile(NamedTuple):
    position: Tup
    velocity: Tup


def tick(world: World, p: Projectile) -> Projectile:
    pos = p.position + p.velocity
    velocity = p.velocity + world.gravity + world.wind
    return Projectile(pos, velocity)


start = point(0, 1, 0)
vel = rt.normalize(vector(1, 1, 0)) * 4
print(vel)
p = Projectile(start, vel)
w = World(vector(0, -0.1, 0), vector(-0.01, 0, 0))

t = 0
while p.position.y > 0:
    print(f"Tick {t}: Position{p.position}")
    p = tick(w, p)
    t = t + 1

print(f"\nTook {t} ticks to hit ground")
