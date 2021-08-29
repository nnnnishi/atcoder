# 耳dp
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/008.jpg
N = int(input())
S = []
for i in range(N):
    S.append(input())

dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(N):
    if S[i] == "AND":
        dp[i + 1][1] += dp[i][1]
        dp[i + 1][0] += 2 * dp[i][0] + dp[i][1]
    else:
        dp[i + 1][1] += dp[i][0] + 2 * dp[i][1]
        dp[i + 1][0] += dp[i][0]

print(dp[N][1])
