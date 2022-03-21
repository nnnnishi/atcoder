# 倍数の性質DP
from functools import lru_cache
import sys

K = int(input())
sys.setrecursionlimit(1000000)

ans = 0
M = 10 ** 9 + 7
if K % 9 != 0:
    exit(print(0))


@lru_cache(maxsize=None)
def dfs(s):
    global ans
    if s == K:
        return 1
    elif s < K:
        for i in range(1, 10):
            if s + i <= K:
                ans += dfs(s + i) % M
        return ans


print(dfs(0) % M)
