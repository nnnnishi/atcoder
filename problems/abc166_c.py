N, M = [int(_) for _ in input().split()]
H = [int(_) for _ in input().split()]
g = [[0] for i in range(N)]

for i in range(M):
    a, b = [int(_) for _ in input().split()]
    g[a - 1].append(H[b - 1])
    g[b - 1].append(H[a - 1])

ans = 0
for i in range(N):
    if H[i] > max(g[i]):
        ans += 1
print(ans)