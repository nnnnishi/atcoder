N, W = [int(_) for _ in input().split()]
dp = [[-1] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0

for n in range(N):
    w, v = [int(_) for _ in input().split()]
    for i in range(W + 1):
        if dp[n][i] >= 0:
            dp[n + 1][i] = max(dp[n][i], dp[n + 1][i])
            if i + w <= W:
                dp[n + 1][i + w] = max(dp[n][i] + v, dp[n + 1][i + w])

print(max(dp[N]))

