N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
MOD = 1000
sumA = sum(A)
if M > sumA:
    exit(print(0))

dp = [[0] * (sumA + 1) for _ in range(N + 1)]
dp[0][0] = 1

for n in range(N):
    for i in range(sumA + 1):
        if dp[n][i] > 0:
            dp[n + 1][i] += dp[n][i]
            dp[n + 1][i] %= MOD
            dp[n + 1][i + A[n]] += dp[n][i]
            dp[n + 1][i + A[n]] %= MOD
print(dp[N][M])

