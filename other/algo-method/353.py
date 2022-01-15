N = int(input())
A = [int(_) for _ in input().split()]
sumA = sum(A)
# dp[桁][合計]=  パターン数
dp = [[0] * (sumA + 1) for _ in range(N + 1)]
dp[0][0] = 1

for n in range(N):
    for i in range(sumA):
        if dp[n][i] > 0:
            dp[n + 1][i] = dp[n][i]
            dp[n + 1][i + A[n]] = 1

# sumAの半分から探索
for i in range(-(-sumA // 2), sumA + 1):
    if dp[N][i] == 1:
        print(i - (sumA - i))
        break
