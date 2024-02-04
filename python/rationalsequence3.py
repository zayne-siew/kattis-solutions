from typing import Tuple

def find(n: int) -> Tuple[int, int]:
    if n == 1:
        return 1, 1
    d, r = divmod(n, 2)
    p, q = find(d)
    if r:
        p += q
    else:
        q += p
    return p, q

for _ in range(int(input())):
    k, n = map(int, input().split())
    p, q = find(n)
    print(f'{k} {p}/{q}')
