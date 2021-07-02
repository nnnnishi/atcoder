from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)


N, K = [int(_) for _ in input().split()]
fix = defaultdict(int)
for i in range(K):
    A, B = [int(_) for _ in input().split()]
    fix[A - 1] = B - 1


@lru_cache(maxsize=None)
def dfs(idx, b1, b2):
    cnt = 0
    if idx == N - 1:
        if idx in fix:
            if fix[idx] == b1 == b2:
                return 0
            else:
                return 1
        elif b1 == b2:
            return 2
        else:
            return 3
    elif b1 == b2:
        if idx in fix:
            if fix[idx] == b1:
                cnt += 0
            else:
                cnt += dfs(idx + 1, fix[idx], b1)
        else:
            for i in range(3):
                if i != b1:
                    cnt += dfs(idx + 1, i, b1)
    else:
        if idx in fix:
            cnt += dfs(idx + 1, fix[idx], b1)
        else:
            for i in range(3):
                cnt += dfs(idx + 1, i, b1)
    return cnt % 10000


print(dfs(0, -1, -2))