from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)


N = int(input())
A = [int(_) for _ in input().split()]
d = Counter(A)
all = 0


for k in d.keys():
    if d[k] >= 2:
        all += d[k] * (d[k] - 1) // 2

for a in A:
    if d[a] < 2:
        print(all)
    elif d[a] == 2:
        print(all - 1)
    else:
        print(all - (d[a] * (d[a] - 1) // 2) + (d[a] - 1) * (d[a] - 2) // 2)

