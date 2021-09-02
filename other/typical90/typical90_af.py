from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [[int(_) for _ in input().split()] for i in range(N)]
M = int(input())
check = set()
for i in range(M):
    x, y = [int(_) for _ in input().split()]
    check.add((x - 1, y - 1))
    check.add((y - 1, x - 1))
ans = 10 ** 8
for p in permutations([i for i in range(N)], N):
    c = True
    for i in range(N - 1):
        if (p[i], p[i + 1]) in check:
            c = False
            break
    if c:
        t = 0
        for l, k in enumerate(p):
            t += A[k][l]
        ans = min(ans, t)
if ans == 10 ** 8:
    print(-1)
else:
    print(ans)