d = {(1, 1): 1}

def find(l: int, r: int) -> int:
    if (l, r) not in d:
        if l > r:  # right child
            n = find(l - r, r)
            d[(l, r)] = 2 * n + 1
        else:  # left child
            n = find(l, r - l)
            d[(l, r)] = 2 * n
    return d[(l, r)]

for _ in range(int(input())):
    k, x = input().split()
    p, q = map(int, x.split('/'))
    print(f'{k} {find(p, q)}')
