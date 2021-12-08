with open('day1in', 'r') as f:
    inp = [int(n) for n in f.readlines() if n.strip()]
# inp = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

c = 0
for i in range(1, len(inp) - 2):
    a = sum(inp[i:i+3])
    b = sum(inp[i-1:i+2])
    if a > b:
        c += 1
print(c)

