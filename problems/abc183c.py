from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = [int(_) for _ in input().split()]
T = [[int(_) for _ in input().split()] for i in range(N)]
toshi = [i for i in range(1, N)]
ans = 0
for L in list(permutations(toshi, N - 1)):
    c = T[0][L[0]]
    for i in range(N - 2):
        c += T[L[i]][L[i + 1]]
    c += T[L[N - 2]][0]
    if c == K:
        ans += 1
print(ans)