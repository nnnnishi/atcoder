from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
d = defaultdict(int)
for i in range(N):
    d[input()] += 1
m = 0
for i in d:
    m = max(m, d[i])
ans = []
for i in d:
    if d[i] == m:
        ans.append(i)

ans.sort()
# print(ans)
for a in ans:
    print(a)
