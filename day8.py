import itertools

with open('day8in', 'r') as f:
    inp = f.readlines()

sp = [l.split(' | ')[1].strip().split(' ') for l in inp] 
lens = [l for l in itertools.chain(*sp)]
print(len([d for d in lens if len(d) in (2, 3, 4, 7)]))
