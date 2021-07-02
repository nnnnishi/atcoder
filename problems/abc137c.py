from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
L = []
ans = 0
for i in range(N):
    S = list(input())
    S.sort()
    L.append("".join(S))
c = Counter(L)
for i in c:
    ans += c[i] * (c[i] - 1) // 2

print(ans)
