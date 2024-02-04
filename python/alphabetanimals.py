from collections import defaultdict
import sys

prev = input()
d = defaultdict(list)

for _ in range(int(input())):
    nxt = input()
    d[nxt[0]].append(nxt)

if not d[prev[-1]]:
    print('?')
    sys.exit(0)
for nxt in d[prev[-1]]:
    if not d[nxt[-1]] or (nxt[0] == nxt[-1] and len(d[nxt[0]]) == 1):
        print(f'{nxt}!')
        break
else:
    print(d[prev[-1]][0])
