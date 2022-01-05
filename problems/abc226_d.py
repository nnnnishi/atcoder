from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import math

N = int(input())
p = []
for _ in range(N):
    l = [int(_) for _ in input().split()]
    p.append(l)
mag_l = set()

for x1, y1 in p:
    for x2, y2 in p:
        dx = x2 - x1
        dy = y2 - y1
        a = math.gcd(dx, dy)
        if dx == 0 and dy == 0:
            continue
        mag_l.add((dx // a, dy // a))

print(len(mag_l))
