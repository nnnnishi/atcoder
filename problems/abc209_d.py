# deque
from collections import deque

N, query = [int(_) for _ in input().split()]
G = [[] for i in range(N)]

for i in range(N - 1):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


# 幅優先
dist = [-1] * N
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


for q in range(query):
    c, d = [int(_) for _ in input().split()]
    if abs(dist[c - 1] - dist[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
