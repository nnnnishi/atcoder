from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S, K = [_ for _ in input().split()]
S = list(S)
K = int(K)
c = set()
for s in permutations(S, len(S)):
    c.add(s)
lc = list(c)
lc.sort()
print("".join(lc[K - 1]))
