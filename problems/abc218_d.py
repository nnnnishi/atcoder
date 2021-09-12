from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
p = []
pset = set()
ans = set()
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    p.append([x, y])
    pset.add((x, y))

for p1, p2 in combinations(p, 2):
    # print(p1, p2)
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    if x1 != y1 and x2 != y2:
        if (x1, y2) in pset and (x2, y1) in pset:
            a = [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]
            a.sort()
            if len(set(a)) == 4:
                ans.add((a[0], a[1], a[2], a[3]))
# print(ans)
print(len(ans))