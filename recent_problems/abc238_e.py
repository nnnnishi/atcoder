import sys

input = sys.stdin.readline
from operator import itemgetter

N, Q = [int(_) for _ in input().split()]
A = []
setA = set(A)
for _ in range(Q):
    X = [int(_) for _ in input().split()]
    setA.add((X[0] - 1, X[1]))
    setA.add((X[1], X[0] - 1))

from collections import Counter, deque, defaultdict

G = [[] for _ in range(N + 1)]

for a, b in setA:
    G[a].append(b)

# 幅優先
dist = [-1] * (N + 1)
Q = deque()
Q.append(0)
dist[0] = 0
while len(Q) > 0:
    # 4辺チェックしキューへ追加
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + 1:
            dist[j] = dist[i] + 1
            Q.append(j)
if dist[N] != -1:
    print("Yes")
else:
    print("No")
