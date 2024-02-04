from itertools import product

r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
colours, curr_colour = {}, 0

for i, j in product(range(r), range(c)):
    if isinstance(grid[i][j], int):
        continue
    curr_colour += 1
    colours[curr_colour] = grid[i][j]
    stack = [(i, j)]

    while stack:
        x, y = stack.pop()
        grid[x][y] = curr_colour
        for nx, ny in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == colours[curr_colour]:
                stack.append((nx, ny))

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    print('neither' if grid[r1 - 1][c1 - 1] != grid[r2 - 1][c2 - 1] else 'binary' if colours[grid[r1 - 1][c1 - 1]] == '0' else 'decimal')
