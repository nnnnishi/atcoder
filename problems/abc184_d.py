from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)


A, B, C = [int(_) for _ in input().split()]

cnt = 0
s = A + B + C


@lru_cache(maxsize=None)
def dfs(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0
    else:
        return (
            (dfs(a + 1, b, c) + 1) * (a) / (a + b + c)
            + (dfs(a, b + 1, c) + 1) * (b) / (a + b + c)
            + (dfs(a, b, c + 1) + 1) * (c) / (a + b + c)
        )


print(dfs(A, B, C))
