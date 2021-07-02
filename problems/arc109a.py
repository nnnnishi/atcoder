from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

a, b, x, y = [int(_) for _ in input().split()]

G = [[] for i in range(200)]
# 上の移動
for i in range(200):
    if i != 99 and i != 199:
        G[i].append((y, i + 1))

# 下の移動
for i in range(200):
    if i != 0 and i != 100:
        G[i].append((y, i - 1))

# 横の移動
for i in range(100):
    G[i].append((x, i + 100))
    G[i + 100].append((x, i))

# 斜めの移動
for i in range(100, 199):
    G[i].append((x, i - 99))
    G[i - 99].append((x, i))

# ダイクストラ
q = []
heappush(q, (0, a - 1))
dist = [-1] * 200
dist[a - 1] = 0
done = [False] * 200
while len(q) > 0:
    d, i = heappop(q)
    if done[i]:
        continue
    done[i] = True
    for d2, j in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + d2:
            dist[j] = dist[i] + d2
            heappush(q, (dist[j], j))
print(dist[b + 100 - 1])
