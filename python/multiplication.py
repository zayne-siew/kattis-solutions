while True:
    a, b = input().split()
    if a == b == '0':
        break
    
    n, m = len(a), len(b)
    s1 = '+' + '-' * (4 * n + 3) + '+'
    s2 = '| ' + '---'.join('+' * (n + 1)) + ' |'
    res = str(int(a) * int(b))
    k = len(res)
    
    print(s1)
    print('   '.join('|' + a + '|'))
    for i, d in enumerate(b):
        if i == 0:
            print(s2)
        nums = [str(int(c) * int(d)).rjust(2, '0') for c in a]
        print('|' + ('/' if n + m - i + 1 <= k else ' ') + '|' + '|'.join((f'{num[0]} /' for num in nums)) + '| |')
        print('| |' + ' / |' * n + d + '|')
        print('|' + (res[k - n - m + i] if n + m - i <= k else ' ') + '|' + '|'.join((f'/ {num[1]}' for num in nums)) + '| |')
        print(s2)
    print('|' + ('/' if k > n else ' ') + ' ' + ' / '.join(res[-n:]) + '    |')
    print(s1)
