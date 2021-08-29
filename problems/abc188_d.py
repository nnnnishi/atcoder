from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, C = [int(_) for _ in input().split()]

day = []
d_c = defaultdict(int)
dset = set()
for i in range(N):
    a, b, c = [int(_) for _ in input().split()]
    d_c[a - 1] += c
    d_c[b] -= c
    if a - 1 not in dset:
        day += [a - 1]
        dset.add(a - 1)
    if b not in dset:
        day += [b]
        dset.add(b)


day.sort()
# print(day)
cost = 0
cb = d_c[day[0]]

for i in range(len(day) - 1):
    dt = day[i + 1] - day[i]
    if cb < C:
        cost += cb * dt
    else:
        cost += C * dt
    cb += d_c[day[i + 1]]
    # print(cb)

print(cost)