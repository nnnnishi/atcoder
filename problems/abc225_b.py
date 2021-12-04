from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
d = defaultdict(int)
ans = set()
for i in range(N - 1):
    a, b = [int(_) for _ in input().split()]
    d[a] += 1
    d[b] += 1
    if d[a] >= 2:
        ans.add(a)
    if d[b] >= 2:
        ans.add(b)
if len(ans) == 1:
    print("Yes")
else:
    print("No")
