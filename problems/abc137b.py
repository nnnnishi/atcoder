from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import numpy as np

N = int(input())
z = [tuple(int(_) for _ in input().split()) for i in range(N)]
ans = 0
zcnt = 0
for zi in permutations(z, N):
    zcnt += 1
    for i in range(N - 1):
        ans += np.linalg.norm(np.array(zi[i + 1]) - np.array(zi[i]))
print(ans / zcnt)
