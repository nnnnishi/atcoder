from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import sys

sys.setrecursionlimit(1000000)

N, Q = [int(_) for _ in input().split()]
graph = []
for i in range(N):
    graph.append([])
for i in range(N - 1):
    e1, e2 = list(map(int, input().split()))
    graph[e1 - 1].append(e2 - 1)
    graph[e2 - 1].append(e1 - 1)

dic = defaultdict(int)
for _ in range(Q):
    p, x = [int(_) for _ in input().split()]
    dic[p - 1] += x


ans = [0] * N


def dfs(i, ttl, boss):
    global ans
    ans[i] += dic[i] + ttl
    for j in graph[i]:
        if j != boss:
            dfs(j, dic[i] + ttl, i)
    return


dfs(0, 0, -1)
print(*ans)