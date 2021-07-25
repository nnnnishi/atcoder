N, M = [int(_) for _ in input().split()]
INF = 10 ** 10
dist = [[INF] * N for _ in range(N)]
for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
