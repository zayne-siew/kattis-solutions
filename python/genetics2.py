import sys

n, m, k = map(int, input().split())
if n == 1:
    print(1)
    sys.exit(0)

def check(s1, s2):
    same = diff = 0
    for ch1, ch2 in zip(s1, s2):
        same += ch1 == ch2
        diff += ch1 != ch2
        if diff > k or same > m - k:
            return False
    return True

ps = [input() for i in range(n)]
i, j = 0, 1
while True:
    if i == n - 1:
        print(i + 1)
        break
    elif not check(ps[i], ps[j]):
        i += 1 + (j - i == 1)
        j = i + 1
    elif i == n - 2:
        for l in range(i):
            ci = check(ps[i], ps[l])
            cj = check(ps[j], ps[l])
            if ci and not cj:
                print(i + 1)
                break
            elif cj and not ci:
                print(j + 1)
                break
        break
    elif j == n - 1:
        print(i + 1)
        break
    else:
        j += 1
