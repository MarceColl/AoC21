from functools import reduce

rev = {'(':')','[':']','{':'}','<':'>'}
sc = {')':1,']':2,'}':3,'>':4}
ov = list(rev.keys())
cv = list(rev.values())

with open('day10in', 'r') as f:
    inp = [l.strip() for l in f.readlines()]

def corrupted(l):
    stack = []
    score = 0
    for i, c in enumerate(l):
        if c in ov:
            stack.append(c)
        else:
            nv = stack.pop()
            if rev[nv] != c:
                return False
        print(c, stack)

    print(list(reversed(stack)))
    return reduce(lambda x, c: x*5 + sc[rev[c]], reversed(stack), 0)


o = [s for s in sorted([corrupted(l) for l in inp]) if s]
print(o)
print(o[int(len(o)/2)])
