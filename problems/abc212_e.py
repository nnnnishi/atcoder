N, M, K = [int(_) for _ in input().split()]
G = []
for _ in range(M):
    u, v = [int(_) for _ in input().split()]
    G.append((u - 1, v - 1))
    G.append((v - 1, u - 1))


MOD = 998244353
dp = [[0] * N for _ in range(K + 1)]
dp[0][0] = 1
for k in range(1, K + 1):
    # 全経路あるとき
    c = sum(dp[k - 1])
    # 引く
    for n1 in range(N):
        dp[k][n1] = (c - dp[k - 1][n1]) % MOD
    for n2 in G:
        dp[k][n2[0]] -= dp[k - 1][n2[1]]
        dp[k][n2[0]] %= MOD
print(dp[K][0])
