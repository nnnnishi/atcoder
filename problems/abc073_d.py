N, M, R = [int(_) for _ in input().split()]
r = [int(_) for _ in input().split()]
INF = 10 ** 10
dist = [[INF] * N for _ in range(N)]
for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ind2r = {}
for i in range(R):
    ind2r[i] = r[i] - 1

# 巡回セールスマン問題 O(N^2*2^N)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c


def has_bit(n, i):
    return (n & 1 << i) > 0


INF = 10 ** 20
ans = INF
for r in range(R):
    dp = [[INF] * R for _ in range(1 << R)]
    # 始点
    dp[0 | (1 << r)][r] = 0
    # おとずれた点の組合せ
    for n in range(1 << R):
        # 前の点
        for i in range(R):
            # つぎの点
            for j in range(R):
                # すでに訪れている、または前と一緒のとき、とばす
                if has_bit(n, j) or i == j:
                    continue
                # 距離が小さくなる時、そのルートを保存
                dp[n | (1 << j)][j] = min(
                    dp[n | (1 << j)][j], dp[n][i] + dist[ind2r[i]][ind2r[j]]
                )
    ans = min(ans, min(dp[(1 << R) - 1]))
# すべてをおとずれて、最後に0にもどる
print(ans)
