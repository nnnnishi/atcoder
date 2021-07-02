from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
P = [0]
for i in range(N):
    P.append(int(input()))

# 2本の矢の点のパターン
Q = set()
for i in P:
    for j in P:
        Q.add(i + j)
Q = list(Q)
Q.sort()
ans = 0
for q in Q:
    rest = M - q
    if M - q >= 0:
        idx = bisect_left(Q, rest)
        if q + Q[idx - 1] <= M:
            ans = max(ans, q + Q[idx - 1])
print(ans)