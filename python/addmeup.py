d = {'1': '1', '2': '2', '5': '5', '6': '9', '8': '8', '9': '6', '0': '0'}
n, s = map(int, input().split())
targets = set()

for x in input().split():
    if s - int(x) in targets:
        print('YES')
        break
    elif all(ch in d for ch in x):
        y = int(''.join(d[ch] for ch in reversed(x)))
        if s - y in targets:
            print('YES')
            break
        targets.add(y)
    targets.add(int(x))
else:
    print('NO')
