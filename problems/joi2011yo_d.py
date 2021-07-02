# 再帰用
import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)
N = int(input())
a = [int(_) for _ in input().split()]


@lru_cache(maxsize=None)
def dfs(i, b_sum):
    cnt = 0
    if i == N - 1:
        if b_sum == a[i]:
            cnt += 1
        return cnt
    elif i == 0:
        cnt += dfs(i + 1, a[i])
        return cnt
    else:
        if 0 <= b_sum - a[i] <= 20:
            cnt += dfs(i + 1, b_sum - a[i])
        if 0 <= b_sum + a[i] <= 20:
            cnt += dfs(i + 1, b_sum + a[i])
        return cnt


print(dfs(0, 0))
