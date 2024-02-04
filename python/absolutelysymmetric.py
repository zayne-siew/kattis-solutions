n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

a = [[0] * n for _ in range(n)]
b = [[0] * n for _ in range(n)]
flag = 1

for i in range(n):
    for j in range(i + 1):
        if i == j:
            a[i][j] = m[i][j]
        elif abs(m[i][j]) == abs(m[j][i]):
            a[i][j] = m[i][j]
            a[j][i] = m[j][i]
        elif (m[i][j] + m[j][i]) % 2:
            flag = -1
            break
        else:
            c = (m[i][j] + m[j][i]) // 2
            a[i][j] = a[j][i] = c
            if c != m[i][j]:
                b[i][j] = m[i][j] - c
                b[j][i] = m[j][i] - c
                flag = 2
    if flag == -1:
        break

print(flag)
if flag != -1:
    print('\n'.join(' '.join(map(str, row)) for row in a))
    if flag == 2:
        print('\n'.join(' '.join(map(str, row)) for row in b))
