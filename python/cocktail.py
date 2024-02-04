n, t = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

curr, end = 0, float('inf')
while lst and curr < end:
    v = lst.pop()
    curr += t
    end = min(end, curr + v)

print('YES' if curr < end else 'NO')
