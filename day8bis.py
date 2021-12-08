#  1111
# 2    3
# 2    3
#  4444
# 5    6
# 5    6
#  7777

num_to_segments = {
    1: {3, 6}, 2: {1,3,4,5,7},
    3: {1,3,4,6,7}, 4: {2,3,4,6},
    5: {1,2,4,6,7}, 6: {1,2,4,5,6,7},
    7: {1,3,6}, 8: {1,2,3,4,5,6,7},
    9: {1,2,3,4,6,7}, 0: {1,2,3,5,6,7},
}

def find_freq(seg):
    values, freq = {v for s in seg for v in s}, {}
    for v in values:
        freq[v] = sum([1 for s in seg if v in s])
    return freq

with open('day8in', 'r') as f:
    inp = f.readlines()

def solve(inp, val):
    inp_freq = find_freq(inp)

    def l(_l):
        return set([n for n in inp if len(n) == _l][0])

    def f(_f):
        return {n for n, nf in inp_freq.items() if nf == _f}

    d1, d4, d7, s47 = l(2), l(4), l(3), f(7)
    s1 = d7 - d1
    segs = [list(s)[0] for s in [s1, f(6), f(8) - s1, s47 - (f(7) - d4), f(4), f(9), s47 - d4]]

    s2n = {}
    for num, numsegs in num_to_segments.items():
        segset = frozenset({segs[n-1] for n in numsegs})
        s2n[segset] = num

    num = [s2n[frozenset(e)] for e in val]
    return sum([n*pow(10,i) for i, n in enumerate(reversed(num))])

print(sum([solve(i.split(' '), val.split(' ')) for l in inp for i, val in [l.strip().split(' | ')]]))

