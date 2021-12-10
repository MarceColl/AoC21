rev = {'(':')','[':']','{':'}','<':'>'}
sc = {')':3,']':57,'}':1197,'>':25137}
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
            if rev[nv] != c and score == 0:
                score = sc[c]

    if score != 0:
        return score
    else:
        return False

print(sum([corrupted(l) for l in inp]))
