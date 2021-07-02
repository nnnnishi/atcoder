N = int(input())
S = []
for i in range(N):
    S.append(int(input()))
dp = [[False] * (100 * 100 + 1) for i in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(100 * 100 + 1):
        if dp[i][j] == True:
            dp[i + 1][j + S[i]] = True
            dp[i + 1][j] = True
for i in range(100 * 100, -1, -1):
    if i % 10 != 0 and dp[N][i]:
        exit(print(i))
print(0)
