from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import numpy as np

N, D = [int(_) for _ in input().split()]
X = [[int(_) for _ in input().split()] for i in range(N)]
ans = 0
for x, y in combinations(X, 2):
    x = np.array(x)
    y = np.array(y)
    u = x - y
    if np.linalg.norm(u) == int(np.linalg.norm(u)):
        ans += 1
print(ans)
