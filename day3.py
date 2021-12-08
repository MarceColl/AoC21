with open('day3in', 'r') as f:
    inp = f.readlines()

h = len(inp)
w = len(inp[0].strip())

d = [[0 for columns in range(h)] for rows in range(w)]

def most_common_bit(col):
    print(sum(d[col]), h)
    if sum(d[col]) > h/2 + 1:
        return 1
    return 0

def to_decimal(n):
    acc = 0
    for i, b in enumerate(reversed(n)):
        acc += b * pow(2,i)
    return acc

for x, l in enumerate(inp):
    for y, b in enumerate(l):
        if b in ('0', '1'):
            d[y][x] = int(b)

gamma = [most_common_bit(i) for i in range(w)]
epsilon = [1-n for n in gamma]
print(gamma)
print(epsilon)

print(to_decimal(gamma) * to_decimal(epsilon))
