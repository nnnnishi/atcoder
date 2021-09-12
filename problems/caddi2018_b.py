from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
d = defaultdict(int)
for i in range(N):
    a = int(input())
    d[i] += a

alleven = True
allone = True
for k in d.keys():
    if d[k] != 1:
        allone = False
    if d[k] % 2 != 0:
        alleven = False

if allone:
    print("first")
elif alleven:
    print("second")
else:
    print("first")

