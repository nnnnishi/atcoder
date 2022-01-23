import sys

input = sys.stdin.readline
# 発電計画問題
T = int(input())
g = [[int(_) for _ in input().split()] for _ in range(T)]

dp = [0] * (T + 2)

for t in range(1, T + 2):
    for i in range(t):
        for j in range(i + 1, t):
            dp[t] = max(dp[t], dp[i] + g[i][j - 1])
    # print(dp)
print(dp[T + 1])
