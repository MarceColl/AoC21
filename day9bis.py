from functools import reduce
import operator

with open('day9in', 'r') as f:
    inp = f.readlines()
    inp = [l.strip() for l in inp]

w = len(inp[0])
h = len(inp)
m = [[int(inp[y][x]) for y in range(h)] for x in range(w)]

def adjacent(x, y):
    adj = set()
    if x > 0:
        adj.add(((x-1, y), m[x-1][y]))
    if x < w - 1:
        adj.add(((x+1, y), m[x+1][y]))
    if y > 0:
        adj.add(((x, y-1), m[x][y-1]))
    if y < h - 1:
        adj.add(((x, y+1), m[x][y+1]))
    return adj

def lowest(x, y):
    return all([val > m[x][y] for coord, val in adjacent(x, y)])

def basin_from(x, y):
    fut = {c for c, v in adjacent(x, y)}
    visited = set([(x, y)])
    size = 1

    while len(fut) > 0:
        coord = fut.pop()
        visited.add(coord)
        if m[coord[0]][coord[1]] != 9:
            fut = fut.union({c for c, v in adjacent(*coord)} - visited)
            size += 1

    return size

basins = reduce(operator.mul, sorted([basin_from(x, y) for x in range(w) for y in range(h) if lowest(x, y)], reverse=True)[0:3], 1)
print(basins)
