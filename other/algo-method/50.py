N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
sumA = sum(A)
if M > sumA:
    exit(print("No"))

# dp[桁][合計]=  パターン数
dp = [[0] * (sumA + 1) for _ in range(N + 1)]
dp[0][0] = 1

for n in range(N):
    for i in range(sumA + 1):
        if dp[n][i] > 0:
            dp[n + 1][i] = 1
            dp[n + 1][i + A[n]] = 1

# sumAの半分から探索
if dp[N][M] == 1:
    print("Yes")
else:
    print("No")
