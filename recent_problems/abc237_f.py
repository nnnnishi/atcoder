# 次元が50程度ならとおる
# https://atcoder.jp/contests/abc044/tasks/arc060_a
N, M = [int(_) for _ in input().split()]
K = M - 1
# dp[idx][0,1,...,k(M-1)]][lcm 0,1,2]= パターン数
dp = [[[0] * 3 for _ in range(K + 1)] for _ in range(N)]
MOD = 998244353
# 1行目
for k in range(K + 1):
    dp[0][k][0] = 1

for idx in range(1, N):
    for k in range(K + 1):
        for bk in range(k):
            for l in range(3):
                if l + 1 <= 2:
                    dp[idx][k][l + 1] += dp[idx - 1][bk][l]
                    dp[idx][k][l + 1] %= MOD
        for bk in range(k, K + 1):
            for l in range(3):
                dp[idx][k][l] += dp[idx - 1][bk][l]
                dp[idx][k][l] %= MOD

ans = 0
for k in range(K + 1):
    ans += dp[N - 1][k][2]
print(dp)
print(ans)
