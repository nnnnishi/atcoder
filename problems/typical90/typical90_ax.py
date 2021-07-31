N, L = [int(_) for _ in input().split()]
M = 10 ** 9 + 7
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    dp[i] += dp[i - 1]
    if i - L >= 0:
        dp[i] += dp[i - L]
    dp[i] %= M
print(dp[N])
