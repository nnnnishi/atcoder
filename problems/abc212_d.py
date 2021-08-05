from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

Q = int(input())
csum = []
a = 0
h = []
for i in range(Q):
    query = [int(_) for _ in input().split()]
    if query[0] == 1:
        heappush(h, (query[1] - a, i))
    elif query[0] == 2:
        a += query[1]
    elif query[0] == 3:
        num, idx = heappop(h)
        # print(csum, idx)
        print(num + csum[i - 1])
    csum.append(a)
