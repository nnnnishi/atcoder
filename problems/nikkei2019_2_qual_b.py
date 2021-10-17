from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
a = [int(_) for _ in input().split()]
M = 998244353
if a[0] != 0:
    exit(print(0))

d = defaultdict(int)
m = 0
for i in range(N):
    if a[i] == 0 and i != 0:
        exit(print(0))
    d[a[i]] += 1
    m = max(m, a[i])

ans = 1
for i in range(m):
    ans *= d[i] ** d[i + 1]
    ans %= M
print(ans)
