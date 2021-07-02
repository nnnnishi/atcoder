N, M = [int(_) for _ in input().split()]
D = [0]
for i in range(N):
    D.append(int(input()))
C = [0]
for i in range(M):
    C.append(int(input()))
INF = 10 ** 10
dp = [[INF] * (N + 1) for _ in range(M + 1)]
dp[0][0] = 0
print(dp)
for j in range(1, M + 1):
    for i in range(N + 1):
        print(i, j)
        dp[j][i] = min(dp[j - 1][i], dp[j - 1][i - 1] + C[j] * D[i])
print(dp[N + 1][M + 1])
