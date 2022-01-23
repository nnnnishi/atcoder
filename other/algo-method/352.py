N, A, B = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]
dp = [[0] * A for _ in range(N + 1)]
dp[0][0] = 1
for n in range(N):
    for i in range(A):
        if dp[n][i] >= 1:
            dp[n + 1][i] += dp[n][i]
            dp[n + 1][(i + X[n]) % A] += dp[n][i]
# print(dp)
if dp[N][B] > 0:
    print("Yes")
else:
    print("No")

