from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]

c = Counter(A)
for i in range(N):
    if i + 1 in c:
        print(c[i + 1])
    else:
        print(0)
