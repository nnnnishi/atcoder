from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

MOD = 10 ** 9 + 7
N = int(input())
a, b = [int(_) for _ in input().split()]
M = int(input())
INF = 10 * 20
dist = [INF] * N
dp = [0] * N
dp[a - 1] = 1
dist[a - 1] = 0
G = [[] for _ in range(N)]
for i in range(M):
    x, y = [int(_) for _ in input().split()]
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)

# 幅優先
Q = deque()
Q.append(a - 1)
dist[a - 1] = 0
while len(Q) > 0:
    # チェックしキューへ追加
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == INF:
            dist[j] = dist[i] + 1
            dp[j] += dp[i]
            Q.append(j)

        elif dist[j] == dist[i] + 1:
            dp[j] += dp[i]
            dp[j] %= MOD
print(dp[b - 1])
