from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

n, k = list(map(int, input().split()))
graph = [[] for i in range(n)]


def check(graph, a, b):
    dist = [-1] * n
    done = [False] * n
    dist[a] = 0
    Q = [(0, a)]
    while len(Q) > 0:
        di, i = heappop(Q)
        if done[i]:
            continue
        done[i] = True
        for g in graph[i]:
            dij = g[1]
            j = g[0]
            if dist[j] == -1 or dist[j] > di + dij:
                dist[j] = di + dij
                heappush(Q, (dist[j], j))

    return dist[b]


ans = []
for i in range(k):
    q = list(map(int, input().split()))
    if q[0] == 0:
        print(check(graph, q[1] - 1, q[2] - 1))
    else:
        graph[q[1] - 1].append((q[2] - 1, q[3]))
        graph[q[2] - 1].append((q[1] - 1, q[3]))
