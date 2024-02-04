nums = [
"""xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx""",
"""....x
....x
....x
....x
....x
....x
....x""",
"""xxxxx
....x
....x
xxxxx
x....
x....
xxxxx""",
"""xxxxx
....x
....x
xxxxx
....x
....x
xxxxx""",
"""x...x
x...x
x...x
xxxxx
....x
....x
....x""",
"""xxxxx
x....
x....
xxxxx
....x
....x
xxxxx""",
"""xxxxx
x....
x....
xxxxx
x...x
x...x
xxxxx""",
"""xxxxx
....x
....x
....x
....x
....x
....x""",
"""xxxxx
x...x
x...x
xxxxx
x...x
x...x
xxxxx""",
"""xxxxx
x...x
x...x
xxxxx
....x
....x
xxxxx"""
]
p = """.....
..x..
..x..
xxxxx
..x..
..x..
....."""

inp = [input() for _ in range(7)]
n = len(inp[0])
exp = ['\n'.join(s[i:i + 5] for s in inp) for i in range(0, n, 6)]
res = str(eval(''.join('+' if s == p else str(nums.index(s)) for s in exp)))
lst = [nums[int(ch)].split('\n') for ch in res]
print('\n'.join('.'.join(ps) for ps in zip(*lst)))