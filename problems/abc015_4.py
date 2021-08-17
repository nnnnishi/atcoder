W = int(input())
N, K = [int(_) for _ in input().split()]
s = []
for i in range(N):
    s.append([int(_) for _ in input().split()])
"""
# dp[i][w][k] = 重要度
dp = [[[-1] * (K + 1) for _ in range(W + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0

ans = 0
for i in range(N):
    for w in range(W + 1):
        for k in range(K + 1):
            dp[i + 1][w][k] = dp[i][w][k]
            if w - s[i][0] >= 0 and k - 1 >= 0:
                if dp[i][w - s[i][0]][k - 1] != -1:
                    dp[i + 1][w][k] = max(
                        dp[i][w][k], dp[i][w - s[i][0]][k - 1] + s[i][1]
                    )
            if i == N - 1:
                ans = max(ans, dp[i + 1][w][k])
"""
# dp[w][k] = 重要度
dp = [[0] * (W + 1) for _ in range(K + 1)]

ans = 0
for i in range(N):
    for k in reversed(range(K)):
        for w in range(W + 1):
            if w + s[i][0] <= W:
                dp[k + 1][w + s[i][0]] = max(dp[k + 1][w + s[i][0]], dp[k][w] + s[i][1])
for k in range(K + 1):
    for w in range(W + 1):
        ans = max(ans, dp[k][w])
# print(dp)
"""
ans = 0
for l in dp[N]:
    ans = max(ans, max(l))
"""
print(ans)
