N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

dp = [[10 ** 10] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        if dp[i][j] != 10 ** 10:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
            if j + A[i] <= M:
                dp[i + 1][j + A[i]] = min(dp[i][j] + 1, dp[i + 1][j + A[i]])


if dp[N][M] != 10 ** 10:
    print(dp[N][M])
else:
    print(-1)
