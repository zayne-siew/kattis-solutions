from functools import lru_cache

s = input()
n = len(s)

@lru_cache(maxsize=None)
def dfs(i: int, curr: int) -> int:
    if i == n:
        return ord('z') - curr
    res = dfs(i + 1, curr)  # skip index i
    if ord(s[i]) > curr:
        res = min(res, dfs(i + 1, ord(s[i])) + ord(s[i]) - curr - 1)
    return res

print(dfs(0, ord('a') - 1))
