# 複数回の選択をゆるすknapsack
# 利得Hを得るのに必要な重量の最小値Wを求める
# https://atcoder.jp/contests/abc153/tasks/abc153_e

N, P = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

dp = [[0, 0] for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    if A[i - 1] % 2 == 0:
        dp[i][0] += dp[i - 1][0] * 2
        dp[i][1] += dp[i - 1][1] * 2
    else:
        dp[i][1] += dp[i - 1][0] + dp[i - 1][1]
        dp[i][0] += dp[i - 1][1] + dp[i - 1][0]
print(dp[N][P])
