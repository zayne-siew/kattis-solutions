import sys

m, d = {}, {}

for line in sys.stdin:
    func, *args = line.split()
    if func == 'clear':
        d.clear()
        m.clear()
    elif func == 'def':
        var, val = args
        if var in m:
            _ = d.pop(m[var])
        m[var] = int(val)
        d[int(val)] = var
    else:
        res, op = 0, '+'
        for arg in args:
            if arg == '+' or arg == '-' or arg == '=':
                op = arg
            elif arg not in m:
                res = 'unknown'
                break
            else:
                res += (-1) ** (op == '-') * m[arg]
        print(*args, d.get(res, 'unknown'))
