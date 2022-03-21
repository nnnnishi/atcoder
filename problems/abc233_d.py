from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = list(map(int, input().split()))
A = [int(_) for _ in input().split()]
cumA = [0] * (N + 1)
for i in range(N):
    cumA[i + 1] = A[i] + cumA[i]
d = defaultdict(int)
ans = 0
for i in range(1, N + 1):
    d[cumA[i - 1]] += 1
    ans += d[cumA[i] - K]

print(ans)
