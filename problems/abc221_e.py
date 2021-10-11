N, M, P = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]

INF = 10 ** 10
V = [INF] * (N + 1)
V[1] = 0

R = [False] * (N + 1)
R[N] = True

for _ in range(N):
    for a, b, c in E:
        if V[a] < INF:
            V[b] = min(V[b], V[a] - c + P)
        if R[b]:
            R[a] = True

for a, b, c in E:
    if V[b] > V[a] - c + P and V[a] < INF and R[a]:
        print(-1)
        exit()

print(max(0, -V[N]))
