from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import math

N, M = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(M):
    A, B, C, D = [int(_) for _ in input().split()]
    if A != B:
        G[A - 1].append((B - 1, C, D))
        G[B - 1].append((A - 1, C, D))

# ダイクストラ法
q = []
heappush(q, (0, 0))
dist = [-1] * N
dist[0] = 0
done = [False] * N
while len(q) > 0:
    D, i = heappop(q)
    if done[i]:
        continue
    done[i] = True
    for j, c, d in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + c + (d // (1 + D)):
            dist[j] = dist[i] + c + (d // (1 + D))

        for t in range(int(math.sqrt(d)) - 5, int(math.sqrt(d)) + 5):
            if t >= D:
                if dist[j] > t + c + (d // (1 + t)):
                    dist[j] = t + c + (d // (1 + t))
        heappush(q, (dist[j], j))

print(dist[N - 1])
