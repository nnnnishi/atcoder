from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

d = {}
d2c = {}

N, K = [int(_) for _ in input().split()]

if N == 0:
    exit(print(0))
check = set()
c = 0
# 重複があるか、K回処理するか
while c < K:
    if N in check:
        break
    check.add(N)
    d[c] = N
    d2c[N] = c
    N += sum(map(int, list(str(N))))
    N %= 100000
    c += 1


if c == K:
    print(N)
else:
    cycle = c - d2c[N]
    res = (K - d2c[N]) % cycle
    print(d[res + d2c[N]])
