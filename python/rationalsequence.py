for _ in range(int(input())):
    k, x = input().split()
    p, q = map(int, x.split('/'))
    
    count = 0  # how many times to travel left
    if p > q:  # right child for one or more generations
        m = (p - 1) // q
        p -= q * m
        count += m
    count += p == q == 1
    
    if q > p:  # left child for one generation
        # travel left upwards, then travel right downwards
        # equivalent to n + 1
        q -= p
        p += q
    q += p * count  # travel left downwards `count` times
    
    print(f'{k} {p}/{q}')
