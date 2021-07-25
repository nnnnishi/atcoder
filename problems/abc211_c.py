# 耳dp
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/008.jpg
S = list(input())
N = len(S)
MOD = 10 ** 9 + 7
dp = [[0] * 8 for _ in range(N + 1)]
d = {}
i = 0
for s in ["c", "h", "o", "k", "u", "d", "a", "i"]:
    d[s] = i
    i += 1

for i in range(1, N + 1):
    for j in range(8):
        dp[i][j] = dp[i - 1][j]
    if S[i - 1] in d:
        if d[S[i - 1]] == 0:
            dp[i][0] += 1
        else:
            dp[i][d[S[i - 1]]] = dp[i - 1][d[S[i - 1]]] + dp[i - 1][d[S[i - 1]] - 1]

print(dp[N][7] % MOD)
