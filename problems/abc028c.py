from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

A = [int(_) for _ in input().split()]
check = []
for c in list(combinations(A, r=3)):
    check.append(c[0] + c[1] + c[2])
check.sort(reverse=True)
print(check[2])
