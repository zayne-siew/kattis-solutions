from collections import defaultdict
from itertools import product
import sys

target = int(input())
if target == 1:
    print(1)
    sys.exit(0)

cache = {2: 2, 11: 2}
queue = defaultdict(set)
queue[2] = {2, 11}
curr_count = 2

def add(curr, count):
    global cache, queue, max_count
    if curr > target or cache.get(curr, count + 1) <= count or cache.get(target, count + 1) <= count:
        return
    cache[curr] = count
    queue[count].add(curr)

while True:
    if target in queue[curr_count]:
        break
    
    for curr in queue[curr_count]:
        if cache.get(curr, curr_count) < curr_count:
            continue

        # Operations with 1: x + 1, x (c) 1, 1 (c) x
        add(curr + 1, curr_count + 1)
        add(curr * 10 + 1, curr_count + 1)
        add(int('1' + str(curr)), curr_count + 1)

        # Operations with y: x + y, x * y, x (c) y. y (c) x
        for prev_count in range(2, curr_count):
            new_count = prev_count + curr_count
            if cache.get(target, new_count + 1) <= new_count:
                continue
            for prev in queue[prev_count]:
                add(prev + curr, new_count)
                add(prev * curr, new_count)
                add(int(str(curr) + str(prev)), new_count)
                add(int(str(prev) + str(curr)), new_count)

    for curr1, curr2 in product(queue[curr_count], repeat=2):
        if cache.get(target, curr_count * 2 + 1) <= curr_count * 2:
            break
        add(curr1 + curr2, curr_count * 2)
        add(curr1 * curr2, curr_count * 2)
        add(int(str(curr1) + str(curr2)), curr_count * 2)
        add(int(str(curr2) + str(curr1)), curr_count * 2)
    
    curr_count += 1

print(curr_count)
