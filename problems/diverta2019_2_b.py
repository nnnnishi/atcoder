from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
b = []
bset = set()
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    b.append([x, y])
    bset.add((x, y))
b.sort()

ans = N
for b1, b2 in combinations(b, 2):
    c = [b1, b2]
    c.sort()
    xdiff = c[0][0] - c[1][0]
    ydiff = c[0][1] - c[1][1]
    xdiff, ydiff
    cnt = 0
    for bx, by in b:
        if (bx + xdiff, by + ydiff) in bset:
            cnt += 1
    ans = min(N - cnt, ans)
print(ans)