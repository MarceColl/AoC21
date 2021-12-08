
with open('day2inbis', 'r') as f:
    inp = f.readlines()

h, d, a = 0, 0, 0

for i in inp:
    cmd, val = i.split(' ')
    val = int(val)

    if cmd == 'forward':
        h += val
        d += val * a
    elif cmd == 'down':
        a += val
    else:
        a -= val

print(d*h)
