import sys
import itertools

#  1111
# 2    3
# 2    3
#  4444
# 5    6
# 5    6
#  7777

num_to_segments = {
    1: {3, 6},
    2: {1,3,4,5,7},
    3: {1,3,4,6,7},
    4: {2,3,4,6},
    5: {1,2,4,6,7},
    6: {1,2,4,5,6,7},
    7: {1,3,6},
    8: {1,2,3,4,5,6,7},
    9: {1,2,3,4,6,7},
    0: {1,2,3,5,6,7},
}

def find_freq(seg):
    values = {v for s in seg for v in s}
    freq = {}
    for v in values:
        freq[v] = 0

        for s in seg:
            if v in s:
                freq[v] += 1
    return freq

num_freq = find_freq(num_to_segments.values())
print(num_freq)

class SegDisp:
    def __init__(self, d):
        self.segment = [set() for i in range(7)]
        self.mapping = dict()
        self.d = d
        self.d_freq = find_freq(self.d)
        self.segs_to_nums = {}

    def gbl(self, l):
        return set([n for n in self.d if len(n) == l][0])

    def gbf(self, f):
        return {n for n, nf in self.d_freq.items() if nf == f}

    def sd(d, s):
        pass

    def solve(self):
        disp1 = self.gbl(2)
        disp7 = self.gbl(3)
        seg1 = disp7 - disp1
        seg2 = self.gbf(6)
        seg3 = self.gbf(8) - seg1
        seg47 = self.gbf(7)
        seg5 = self.gbf(4)
        seg6 = self.gbf(9)

        d4 = self.gbl(4)
        seg4 = seg47 - d4
        seg7 = seg47 - seg4

        segs = [seg1, seg2, seg3, seg7, seg5, seg6, seg4]
        segs = [list(s)[0] for s in segs]

        self.seg_to_nums = {}
        for num, numsegs in num_to_segments.items():
            segset = frozenset({segs[n-1] for n in numsegs})
            self.seg_to_nums[segset] = num

    def translate(self, l):
        num = [self.seg_to_nums[frozenset(e)] for e in l]
        return sum([n*pow(10,i) for i, n in enumerate(reversed(num))])

inp = ["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"]
val = ["fgae", "cfgab", "fg", "bagce"]

with open('day8in', 'r') as f:
    inp = f.readlines()

acc = 0
for l in inp:
    inp, val = l.strip().split(' | ')
    inp = inp.split(' ')
    val = val.split(' ')

    d = SegDisp(inp)
    d.solve()
    acc += d.translate(val)

print(acc)


