N, M = [int(_) for _ in input().split()]
G = [[] for i in range(N)]
INF = 10 ** 9
dist = [[INF] * N for i in range(N)]
for i in range(M):
    a, b, t = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    dist[a - 1][b - 1] = t
    dist[b - 1][a - 1] = t

for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = 10 ** 9
for l in dist:
    ans = min(ans, max(l))
print(ans)