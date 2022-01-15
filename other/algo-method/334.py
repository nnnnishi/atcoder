import sys

input = sys.stdin.readline
N = int(input())
A = [[int(_) for _ in input().split()] for i in range(N)]
# print(A)
dp = [[0] * N for _ in range(N)]
dp[0][0] = A[0][0]
for i in range(N):
    if i == 0:
        for j in range(N):
            if j != 0:
                dp[i][j] += dp[i][j - 1] + A[i][j]
    else:
        for j in range(N):
            if j != 0:
                dp[i][j] += max(dp[i][j - 1], dp[i - 1][j]) + A[i][j]
            else:
                dp[i][j] += dp[i - 1][j] + A[i][j]
print(dp[N - 1][N - 1])

