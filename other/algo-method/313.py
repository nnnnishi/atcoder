# 個数制限付き部分和問題
# O(NM)
# https://algo-method.com/tasks/313/editorial
import sys

input = sys.stdin.readline

N, M = [int(_) for _ in input().split()]
A = []
B = []
for _ in range(N):
    a, b = [int(_) for _ in input().split()]
    A.append(a)
    B.append(b)

dp = [[10 ** 10] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        if dp[i][j] != 10 ** 10:
            dp[i + 1][j] = 0
        if j >= A[i]:
            if dp[i][j - A[i]] < 10 ** 10:
                dp[i + 1][j] = min(dp[i + 1][j], 1)
            if dp[i + 1][j - A[i]] < B[i]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - A[i]] + 1)

if dp[N][M] != 10 ** 10:
    print("Yes")
else:
    print("No")
