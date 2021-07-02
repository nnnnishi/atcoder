from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
Z = [0] * N
Z[0] = 1
idx = 0
for i in range(1, N):
    if A[i] != A[i - 1]:
        Z[idx] += 1
    else:
        idx += 1
        Z[idx] += 1
sumZ = list(accumulate([0] + Z))
ans = 0
for i in range(3, N + 1):
    ans = max(ans, sumZ[i] - sumZ[i - 3])
if N == 2:
    ans = sum(Z)
print(ans)
