from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations


def has_bit(n, i):
    return n & (1 << i) > 0


N, T = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
Nf = N // 2
Af = A[:Nf]
Aa = A[Nf:]
Na = len(Aa)

totAfL = []
for n in range(1 << Nf):
    totAf = 0
    for i in range(Nf):
        if has_bit(n, i):
            totAf += Af[i]
    totAfL.append(totAf)
totAfL.sort()

# 半分全探索
ans = 0
for n in range(1 << Na):
    totAa = 0
    for i in range(Na):
        if has_bit(n, i):
            totAa += Aa[i]
    rest = T - totAa
    if rest >= 0:
        idx = bisect_right(totAfL, rest)
        ans = max(ans, totAfL[idx - 1] + totAa)

print(ans)
