n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)

res = 0
q, r = divmod(n, 3)
for i in range(q):
    res += lst[3 * i] + lst[3 * i + 1]
for i in range(r):
    res += lst[~i]

print(res)
