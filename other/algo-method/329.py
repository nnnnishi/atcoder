import sys

input = sys.stdin.readline
N = int(input())
A = [list(input()) for _ in range(N)]
# print(A)
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    if i == 0:
        for j in range(N):
            if j != 0:
                if A[i][j - 1] == ".":
                    dp[i][j] += dp[i][j - 1]
    else:
        for j in range(N):
            if j != 0:
                if A[i][j - 1] == ".":
                    dp[i][j] += dp[i][j - 1]
                if A[i - 1][j] == ".":
                    dp[i][j] += dp[i - 1][j]
            else:
                if A[i - 1][j] == ".":
                    dp[i][j] += dp[i - 1][j]
print(dp[N - 1][N - 1])

