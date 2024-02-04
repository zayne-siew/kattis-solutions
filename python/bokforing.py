from collections import defaultdict

n, q = map(int, input().split())
d = defaultdict(int)
for _ in range(q):
    cmd, *args = input().split()
    if cmd == 'SET':
        person, capital = map(int, args)
        d[person] = capital
    elif cmd == 'PRINT':
        print(d[int(args[0])])
    else:
        v = int(args[0])
        d = defaultdict(lambda: v)
