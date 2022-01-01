from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
d = Counter(A)
print(d[1] * (d[1] - 1) // 2 + d[2] * (d[2] - 1) // 2 + d[3] * (d[3] - 1) // 2)

