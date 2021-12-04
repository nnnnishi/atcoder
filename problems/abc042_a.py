from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

c = Counter([int(_) for _ in input().split()])

if c[5] == 2 and c[7] == 1:
    print("YES")
else:
    print("NO")

