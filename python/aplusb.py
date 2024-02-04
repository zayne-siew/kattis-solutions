n = int(input())
lst = [int(x) for x in input().split()]
lst.sort()

res = 0
k = n - 1
while k >= 0:
    i, j = 0, k
    while lst[j] == lst[k]:
        j -= 1
    tmp, count = 0, k - j
    while i < j:
        if lst[i] + lst[j] == lst[k]:
            i1 = i
            while lst[i1] == lst[i]:
                i += 1
            if lst[i1] == lst[j]:
                tmp += (i - i1) * (i - i1 - 1)  # (i - i1)C2 * 2
                break
            j1 = j
            while lst[j1] == lst[j]:
                j -= 1
            tmp += (i - i1) * (j1 - j) * 2
        elif lst[i] + lst[j] < lst[k]:
            i1 = i
            while lst[i1] == lst[i]:
                i += 1
        else:
            j1 = j
            while lst[j1] == lst[j]:
                j -= 1
    res += tmp * count
    k1 = k
    while lst[k1] == lst[k]:
        k -= 1

print(res)
