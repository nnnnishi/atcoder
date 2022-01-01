from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

n, x = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
for ai in a:
    if x == ai:
        print("Yes")
        exit()
print("No")
