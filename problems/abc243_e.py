N, M = [int(_) for _ in input().split()]
INF = 10 ** 20

dist = [[INF] * N for _ in range(N)]
e = []
for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    e.append([c, a - 1, b - 1])
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = 0
for c, i, j in e:
    for k in range(N):
        if c >= dist[i][k] + dist[k][j]:
            ans += 1
            break

print(ans)

