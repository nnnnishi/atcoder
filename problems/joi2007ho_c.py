from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
Q = []
for _ in range(N):
    x, y = [int(_) for _ in input().split()]
    Q.append((x, y))
Qset = set(Q)
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = Q[i]
        x2, y2 = Q[j]
        vec_x = x2 - x1
        vec_y = y2 - y1
        x3 = x2 - vec_y
        y3 = y2 + vec_x
        x4 = x1 - vec_y
        y4 = y1 + vec_x
        if (x3, y3) in Qset and (x4, y4) in Qset:
            tmp = ((x3 - x1) ** 2 + (y3 - y1) ** 2) // 2
            ans = max(ans, tmp)
print(ans)