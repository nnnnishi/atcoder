# bitDP:O(3^N) -> N = 15で1000万程度
# dp[すでに選んだ点の集合][現在のグループ数] = スコアの最小値
# https://twitter.com/e869120/status/1395510657634619394/photo/1

inf = 10 ** 20
n, k = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]

# すべてのペアの2点間距離を求める
dist = [[0] * n for _ in range(n)]
for i in range(n):
    x0, y0 = xy[i]
    for j in range(i):
        x1, y1 = xy[j]
        d = (x0 - x1) ** 2 + (y0 - y1) ** 2
        dist[i][j] = dist[j][i] = d

# すべての集合についてコスト（2点間距離の最大値）を求める
popcnt = lambda x: bin(x).count("1")
max_dist = [0] * (1 << n)
for bit in range(1 << n):
    if popcnt(bit) < 2:
        continue
    i = bit.bit_length() - 1
    d = max_dist[bit ^ 1 << i]
    for j in range(n):
        # jを含んでいたらそれまでの最大値dとその距離dist[i][j]を比べる
        if bit >> j & 1:
            d = max(d, dist[i][j])
    max_dist[bit] = d

# dp更新用関数
def chmin(bit, i, val):
    if val < dp[bit][i]:
        dp[bit][i] = val


# dp[bit][i]...i個のグループで集合bitを作るときの最小コスト
dp = [[inf] * (k + 1) for _ in range(1 << n)]
dp[0][0] = 0
mask = (1 << n) - 1
for bit in range(1 << n):
    # 0グループからkグループまで回す
    for i in range(k):
        pre = dp[bit][i]
        if pre == inf:
            continue
        # bitの補集合をs0として、s0の部分集合sを列挙してdpを更新する
        s0 = s = mask ^ bit
        while s:
            chmin(bit | s, i + 1, max(pre, max_dist[s]))
            s = (s - 1) & s0

print((dp[(1 << n) - 1][k]))
