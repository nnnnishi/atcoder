# 連結DP
# https://atcoder.jp/contests/abc248/tasks/abc248_f
N, P = [int(_) for _ in input().split()]

# dp[j本][つながっているか]= パターン数
dp = [[0, 0] for _ in range(N)]
dp[1][0] = 1
dp[0][1] = 1
for n in range(1, N):
    ndp = [[0, 0] for _ in range(N)]
    for j in range(N):
        dp0 = dp[j][0]
        dp1 = dp[j][1]
        # 削除しない
        ndp[j][1] += dp0 + dp1
        # 連結→非連結
        if j + 2 < N:
            ndp[j + 2][0] += 2 * dp1
        if j + 1 < N:
            # 連結→連結
            ndp[j + 1][1] += 2 * dp1
            # 上下
            ndp[j + 1][1] += dp1
            ndp[j + 1][0] += dp0
        for k in range(3):
            if j + k < N:
                ndp[j + k][0] %= P
                ndp[j + k][1] %= P
    dp = ndp.copy()
print(*[dp[i][1] for i in range(1, N)])
