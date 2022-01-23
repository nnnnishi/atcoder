N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
# dp[桁][合計]=  パターン数
dp = [[0] * (M) for _ in range(N)]
dp[0][0] = 1
for n in range(N - 1):
    for i in range(M):
        if dp[n][i] > 0:
            dp[n + 1][i] = dp[n][i]
            if i + A[n] <= M - 1:
                dp[n + 1][i + A[n]] = 1

# sumAの半分から探索
# print(dp)
print(sum(dp[N - 1]))

