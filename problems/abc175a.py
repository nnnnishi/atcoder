from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import numpy as np

N = int(input())
L = [int(_) for _ in input().split()]
ans = 0
for a, b, c in combinations(L, 3):
    l = [a, b, c]
    if len(set(l)) == 3:
        l.sort()
        if l[0] + l[1] > l[2]:
            ans += 1
print(ans)
