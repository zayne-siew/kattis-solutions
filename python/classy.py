def get_rank(clss):
    d = {'upper': 0, 'middle': 1, 'lower': 2}
    res = 0
    clss = clss.split('-')
    for sub in reversed(clss):
        res = res * 3 + d[sub]
    for _ in range(10 - len(clss)):
        res = res * 3 + d['middle']
    return res

for _ in range(int(input())):
    people = []
    for _ in range(int(input())):
        name, clss, _ = input().split()
        people.append((get_rank(clss), name[:-1]))
    people.sort()
    print(*map(lambda p: p[1], people), sep='\n')
    print('=' * 30)
