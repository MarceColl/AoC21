from collections import defaultdict

with open('day5in', 'r') as f:
    inp = f.readlines()

m = defaultdict(lambda: 0)

def parse_line(l):
    coords = [tuple([int(n) for n in c.strip().split(',')]) for c in l.split('->')]
    assert len(coords) == 2
    return coords

def clamp(n):
    return min(1, max(n, -1))

def get_line(fr, to):
    dx = to[0] - fr[0]
    dy = to[1] - fr[1]
    while dx != 0 or dy != 0:
        yield to[0] - dx, to[1] - dy
        dx -= clamp(dx)
        dy -= clamp(dy)

    yield to[0], to[1]

coords = [parse_line(l) for l in inp]

for fr, to in coords:
    for x, y in get_line(fr, to):
        m[(x, y)] += 1

print(sum([1 for n in m.values() if n > 1]))
