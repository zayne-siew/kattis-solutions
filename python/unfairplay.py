rs = [0, 1, 2]

while True:
    s = input()
    if s == '-1':
        break
    n, m = map(int, s.split())
    teams = [int(x) for x in input().split()]
    
    matches, res = [], []
    for _ in range(m):
        a, b = map(int, input().split())
        if a == n or b == n:
            matches.append(None)
            res.append('0' if a == n else '2')
            teams[-1] += 2
        else:
            matches.append((a - 1, b - 1))
            res.append(None)

    def dfs(curr):
        global teams, res
        if curr == m:
            return True
        elif matches[curr] is None:
            return dfs(curr + 1)
        a, b = matches[curr]
        for r in rs:
            if teams[a] + 2 - r >= teams[-1] or teams[b] + r >= teams[-1]:
                continue
            teams[a] += 2 - r
            teams[b] += r
            res[curr] = str(r)
            if dfs(curr + 1):
                return True
            teams[a] -= 2 - r
            teams[b] -= r
        return False

    if dfs(0):
        print(' '.join(res))
    else:
        print('NO')
    _ = input()
