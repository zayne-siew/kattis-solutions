for _ in range(int(input())):
    n, *grades = map(int, input().split())
    ave = sum(grades) / n
    print(f'{sum(grade > ave for grade in grades) / n * 100:.3f}%')
