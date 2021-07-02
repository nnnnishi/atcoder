from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M, Q = [int(_) for _ in input().split()]
LR = []
sumLR = []
# idxをそろえる
for i in range(N + 1):
    LR.append([0] * (N + 1))

for i in range(M):
    L, R = [int(_) for _ in input().split()]
    LR[L][R] += 1
# 累積和
for l in range(N + 1):
    sumLR.append(list(accumulate(LR[l])))

for _ in range(Q):
    ans = 0
    p, q = [int(_) for _ in input().split()]
    for l in range(p, q + 1):
        ans += sumLR[l][q]
    print(ans)
