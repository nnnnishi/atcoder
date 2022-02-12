from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
S = list(input())
M = 10 ** 9 + 7
dp = [[1] * (N + 1)] + [[0] * (N + 1) for _ in range(7)]
for i, s in enumerate(list("atcoder")):
    for j in range(1, N + 1):
        if S[j - 1] == s:
            dp[i + 1][j] = dp[i][j - 1] + dp[i + 1][j - 1]
        else:
            dp[i + 1][j] = dp[i + 1][j - 1]
        dp[i + 1][j] %= M
print(dp[7][N])

