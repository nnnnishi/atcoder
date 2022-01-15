N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
dp = [[-1] * M for _ in range(N)]
dp[0][0] = 0
for n in range(N - 1):
    for i in range(M):
        if dp[n][i] >= 0:
            dp[n + 1][i] = dp[n][i]
        if i - A[n] >= 0 and dp[n][i - A[n]] >= 0:
            dp[n + 1][i] = max(dp[n + 1][i], dp[n][i - A[n]] + B[n])

print(dp[N - 1][M - 1])

