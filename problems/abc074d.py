from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
dist = [[int(_) for _ in input().split()] for i in range(N)]

ans = 0
for i, j in combinations(range(N), r=2):
    ok_flg = True
    for k in range(N):
        if k != i and k != j:
            if dist[i][j] > dist[i][k] + dist[k][j]:
                exit(print(-1))
            elif dist[i][j] == dist[i][k] + dist[k][j]:
                ok_flg = False
                break
    if ok_flg:
        ans += dist[i][j]

if ans == 0:
    print(-1)
else:
    print(ans)
