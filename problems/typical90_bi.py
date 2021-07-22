from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

Q = deque()

N = int(input())
for i in range(N):
    t, x = [int(_) for _ in input().split()]
    if t == 1:
        Q.appendleft(x)
    elif t == 2:
        Q.append(x)
    else:
        print(Q[x - 1])
