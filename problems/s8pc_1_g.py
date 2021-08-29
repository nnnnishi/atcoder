N, M = [int(_) for _ in input().split()]

INF = 10 ** 15
D = [[INF] * N for _ in range(N)]
T = [[INF] * N for _ in range(N)]
for i in range(M):
    s, t, d, time = [int(_) for _ in input().split()]
    s -= 1
    t -= 1
    D[s][t] = d
    D[t][s] = d
    T[s][t] = time
    T[t][s] = time


def has_bit(n, i):
    return (n & 1 << i) > 0


dp = [[INF] * N for _ in range(1 << N)]
pat = [[0] * N for _ in range(1 << N)]

# 0を始点とする
dp[0][0] = 0
pat[0][0] = 1
ans = INF
cnt = 0
# おとずれた点の組合せ
for n in range(1 << N):
    # 前の点
    for i in range(N):
        # つぎの点
        for j in range(N):
            # すでに訪れている、または前と一緒のとき、とばす
            if has_bit(n, j) or i == j:
                continue
            # 距離が小さくなる時、そのルートを保存
            if D[i][j] != INF and dp[n][i] + D[i][j] <= T[i][j]:
                if dp[n][i] + D[i][j] == dp[n | (1 << j)][j]:
                    pat[n | (1 << j)][j] += pat[n][i]
                elif dp[n][i] + D[i][j] < dp[n | (1 << j)][j]:
                    pat[n | (1 << j)][j] = pat[n][i]
                    dp[n | (1 << j)][j] = dp[n][i] + D[i][j]

# print(pat)
# print(dp)
if pat[(1 << N) - 1][0] == 0:
    print("IMPOSSIBLE")
else:
    print(dp[(1 << N) - 1][0], pat[(1 << N) - 1][0])
