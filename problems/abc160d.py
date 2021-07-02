from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, X, Y = [int(_) for _ in input().split()]
G = [[] for i in range(N)]
for i in range(N - 1):
    G[i].append((1, i + 1))
    G[i + 1].append((1, i))
G[X - 1].append((1, Y - 1))
G[Y - 1].append((1, X - 1))

# ダイクストラ
def calc_dist(n):
    q = []
    dist = [-1] * N
    heappush(q, (0, n))
    dist[n] = 0
    done = [False] * N
    while len(q) > 0:
        d, i = heappop(q)
        if done[i]:
            continue
        done[i] = True
        for d2, j in G[i]:
            if dist[j] == -1 or dist[j] > d + d2:
                dist[j] = dist[i] + d2
                heappush(q, (dist[j], j))

    return dist


L = []
for z in range(N - 1):
    L += calc_dist(z)[z + 1 :]
c = Counter(L)
for k in range(1, N):
    print(c[k])