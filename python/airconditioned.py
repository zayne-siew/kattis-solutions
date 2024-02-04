n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda t: (t[0], -t[1]))

res = 1
lo, hi = lst[0]
for a, b in lst[1:]:
    if a > hi:
        res += 1
        lo, hi = a, b
    elif b < hi:
        hi = b

print(res)
