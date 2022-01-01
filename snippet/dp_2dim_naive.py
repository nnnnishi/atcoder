N, S = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
# dp[桁][合計]=  パターン数
dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1

for n in range(N):
    for i in range(S + 1):
        if dp[n][i] > 0:
            dp[n + 1][i] = dp[n][i]
            if i + A[n] <= S:
                dp[n + 1][i + A[n]] += dp[n][i]

if dp[N][S] > 0:
    print("Yes")
else:
    print("No")
