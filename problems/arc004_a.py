from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import math

N = int(input())
A = []
for i in range(N):
    A.append([int(_) for _ in input().split()])
ans = 0
for a, b in combinations(A, 2):
    ans = max(ans, (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
print(math.sqrt(ans))
