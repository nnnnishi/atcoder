from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for i in range(N)]
ans = 0
for i, j in combinations(range(M), 2):
    cnt = 0
    for k in range(N):
        cnt += max(A[k][i], A[k][j])
    ans = max(cnt, ans)
print(ans)