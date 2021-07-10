# 次元が50程度ならとおる
# https://atcoder.jp/contests/abc044/tasks/arc060_a
N, A = [int(_) for _ in input().split()]
x = [int(_) for _ in input().split()]
# dp[桁][いれたかず][合計]=  パターン数
dp = [[[0] * (N * 50 + 1) for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
for n in range(N):
    for i in range(N + 1):
        for j in range(N * 50 + 1):
            # いれない
            dp[n + 1][i][j] = dp[n][i][j] + dp[n + 1][i][j]
            # いれる
            if i - 1 >= 0 and j - x[n] >= 0:
                dp[n + 1][i][j] = dp[n][i - 1][j - x[n]] + dp[n + 1][i][j]
ans = 0
i = 1
while A * i < (N * 50 + 1) and i < (N + 1):
    ans += dp[N][i][i * A]
    i += 1
print(ans)