N = int(input())
# dp[桁][合計]=  パターン数
dp = [[0] * 9 for _ in range(N + 1)]
for i in range(9):
    dp[0][i] = 1
M = 998244353
for n in range(1, N):
    for i in range(9):
        if i == 0:
            dp[n][i] = dp[n - 1][i] + dp[n - 1][i + 1]
        elif i == 8:
            dp[n][i] = dp[n - 1][i] + dp[n - 1][i - 1]
        else:
            dp[n][i] = dp[n - 1][i] + dp[n - 1][i - 1] + dp[n - 1][i + 1]
        dp[n][i] %= M
print(sum(dp[N - 1]) % M)
