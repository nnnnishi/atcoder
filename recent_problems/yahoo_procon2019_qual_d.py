from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
check = []
for _ in range(N):
    check.append(int(input()))

dp0 = [0] * N
for i in range(N):
    if check[i] == 0:
        dp0[i] = 0
    else:
        dp0[i] = check[i]
dp1 = [0] * N
for i in range(N):
    if check[i] == 0:
        dp1[i] = 1
    elif check[i] % 2 == 1:
        dp1[i] = 0
    else:
        dp1[i] = 1
dp2 = [0] * N
for i in range(N):
    if check[i] == 0:
        dp2[i] = 2
    elif check[i] % 2 == 1:
        dp2[i] = 1
    else:
        dp2[i] = 0
S = []
for l in [dp0, dp2, dp1, dp2, dp0]:
    x = l.copy()
    S.append(x)

ans = 10 ** 20
for i in range(5):
    for j in range(1, N):
        cand = []
        for k in range(i + 1):
            cand.append(S[i - k][j - 1])
        S[i][j] += min(cand)
    if ans > S[i][N - 1]:
        ans = S[i][N - 1]
print(ans)
