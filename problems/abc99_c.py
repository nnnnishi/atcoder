N = int(input())
m = set()
c = 0
while 6 ** c <= N:
    m.add(6 ** c)
    c += 1
c = 0
while 9 ** c <= N:
    m.add(9 ** c)
    c += 1
m = list(m)
m.sort()
lenc = len(m)


dp = [[-1] * (N + 1) for _ in range(lenc + 1)]
dp[0][0] = 0

for i in range(1, lenc + 1):
    dp[i][0] = 0
    for j in range(N, -1, -1):
        k = 0
        dp[i][j] = dp[i - 1][j]
        while j - (k + 1) * m[i - 1] >= 0 and k <= 9:
            k += 1
            if dp[i - 1][j - (k * m[i - 1])] >= 0:
                if dp[i][j] == -1:
                    dp[i][j] = dp[i - 1][j - (k * m[i - 1])] + k
                else:
                    dp[i][j] = min(dp[i][j - (k * m[i - 1])] + k, dp[i][j])

print(dp[lenc][N])
