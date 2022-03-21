import copy

MOD = 998244353
N, M, K, S, T, X = [int(_) for _ in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(_) for _ in input().split()]
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
dp = [[[0, 0] for _ in range(N)] for _ in range(K + 1)]
dp[0][S - 1][0] = 1
for i in range(K):
    for n in range(N):
        for k in range(2):
            if dp[i][n][k] > 0:
                for nx in G[n]:
                    if nx != (X - 1):
                        dp[i + 1][nx][k] += dp[i][n][k]
                        dp[i + 1][nx][k] %= MOD
                    else:
                        dp[i + 1][nx][(k + 1) % 2] += dp[i][n][k]
                        dp[i + 1][nx][(k + 1) % 2] %= MOD
print(dp[K][T - 1][0])
