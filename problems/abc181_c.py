from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = []
for i in range(N):
    A.append([int(_) for _ in input().split()])

for x in list(combinations(A, 3)):
    if (x[0][0] - x[1][0]) * (x[0][1] - x[2][1]) == (x[0][0] - x[2][0]) * (
        x[0][1] - x[1][1]
    ):
        exit(print("Yes"))
else:
    print("No")
