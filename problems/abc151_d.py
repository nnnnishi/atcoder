Y, X = [int(_) for _ in input().split()]
A = [list(input()) for i in range(Y)]
N = X * Y

INF = 10 ** 10
dist = [[INF] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for y in range(Y):
    for x in range(X):
        if x != X - 1 and A[y][x] == "." and A[y][x + 1] == ".":
            dist[X * y + x][X * y + (x + 1)] = 1
            dist[X * y + (x + 1)][X * y + x] = 1
        if y != Y - 1 and A[y][x] == "." and A[y + 1][x] == ".":
            dist[X * y + x][X * (y + 1) + x] = 1
            dist[X * (y + 1) + x][X * y + x] = 1

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for i in range(N):
    for j in range(i, N):
        if dist[i][j] != INF:
            ans = max(ans, dist[i][j])
print(ans)