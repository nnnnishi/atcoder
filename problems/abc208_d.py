from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
dist = [[-1] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0

for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    dist[a - 1][b - 1] = c

ans = 0
for k in range(N):
    for s in range(N):
        for t in range(N):
            if dist[s][k] != -1 and dist[k][t] != -1:
                if dist[s][t] == -1:
                    dist[s][t] = dist[s][k] + dist[k][t]
                if dist[s][t] > dist[s][k] + dist[k][t]:
                    dist[s][t] = dist[s][k] + dist[k][t]
    for s in range(N):
        for t in range(N):
            if dist[s][t] != -1:
                ans += dist[s][t]
print(ans)
