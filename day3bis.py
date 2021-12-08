with open('day3in', 'r') as f:
    inp = [[int(n) for n in list(l.strip())] for l in f.readlines()]

def to_decimal(n):
    return sum([b*pow(2, i) for i, b in enumerate(reversed(n))])

def mcb(c, vals):
    num_ones = sum([n[c] for n in vals]) 
    if num_ones >= len(vals)/2:
        return 1
    else:
        return 0

def lcb(c, vals):
    return 1 - mcb(c, vals)

def find(f):
    nums = inp
    for c in range(len(inp[0])):
        b = f(c, nums)
        nums = [n for n in nums if n[c] == b]
        if len(nums) == 1:
            return nums[0]

ogr = to_decimal(find(mcb))
csr = to_decimal(find(lcb))

print(ogr * csr)

