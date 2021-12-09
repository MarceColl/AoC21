with open('day9in', 'r') as f:
    inp = f.readlines()
    inp = [l.strip() for l in inp]

w = len(inp[0])
h = len(inp)
m = [[int(inp[y][x]) for y in range(h)
        if inp[y][x] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')] 
        for x in range(w)]

def lowest(x, y):
    res = True
    print(x,y, w, h)
    if x > 0:
        res = res and m[x-1][y] > m[x][y]
    if x < w - 1:
        res = res and m[x+1][y] > m[x][y]
    if y > 0:
        res = res and m[x][y-1] > m[x][y]
    if y < h - 1:
        res = res and m[x][y+1] > m[x][y]
    return res


risk = sum([m[x][y] + 1 for x in range(w) for y in range(h) if lowest(x, y)])
print(risk)
