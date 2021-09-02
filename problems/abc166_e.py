from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
a = [int(_) for _ in input().split()]
ai = defaultdict(int)
aj = defaultdict(int)
for i in range(N):
    ai[i - a[i]] += 1
    aj[i + a[i]] += 1

ans = 0
for k in ai.keys():
    if k in aj:
        ans += ai[k] * aj[k]
print(ans)