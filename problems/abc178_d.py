from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)

MOD = 10 ** 9 + 7


@lru_cache(maxsize=None)
def dfs(n):
    if n < 0 or 1 <= n <= 2:
        return 0
    elif n == 0:
        return 1
    else:
        return dfs(n - 3) + dfs(n - 1)


N = int(input())
print(dfs(N) % MOD)
