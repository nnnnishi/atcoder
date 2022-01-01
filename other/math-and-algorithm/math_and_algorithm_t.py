from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
d = Counter(A)
ans = 0
for k in set(A):
    if k == 50000:
        if d[k] >= 2:
            ans += (d[k] * (d[k] - 1)) // 2
    else:
        ans += d[k] * d[100000 - k]
    d[100000 - k] = 0
    d[k] = 0
print(ans)
