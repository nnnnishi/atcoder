N = int(input())

# dp[頂点i][前の頂点の色][1の色] = パターン数
INF = 10 ** 10
dp = [[[INF, INF], [INF, INF]] for _ in range(N + 1)]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

# 1番目を0
dp[1][0][0] = A[1]
# 1番目を1
dp[1][1][1] = 0

for i in range(2, N):
    for j in range(2):
        for k in range(2):
            for prej in range(2):
                if j == 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][prej][k] + A[i])
                elif j == prej:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][prej][k] + B[i - 1])
                else:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][prej][k])
print(dp)
ans = INF
for j in range(2):
    for k in range(2):
        if j == k:
            ans = min(ans, dp[N - 1][j][k] + B[N - 1])
        else:
            ans = min(ans, dp[N - 1][j][k])
print(ans)
