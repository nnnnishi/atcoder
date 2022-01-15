N, M = [int(_) for _ in input().split()]
W = [int(_) for _ in input().split()]
V = [int(_) for _ in input().split()]
dp = [[-1] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for n in range(N):
    for i in range(M + 1):
        if dp[n][i] >= 0:
            dp[n + 1][i] = dp[n][i]
        if i - W[n] >= 0 and dp[n][i - W[n]] >= 0:
            dp[n + 1][i] = max(dp[n + 1][i], dp[n][i - W[n]] + V[n])

print(max(dp[N]))

