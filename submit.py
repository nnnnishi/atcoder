# 再帰用
import sys

sys.setrecursionlimit(1000000)

# itertools
import itertools
for x,y in itertools.product(range(101),repeat = 2):



# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 深さ優先
def dfs(i):
    global ans
    y = i[0]
    x = i[1]
    if y == gy and x == gx:
        ans = True
    v[y][x] = False
    for y2, x2 in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
        if 0 <= x2 < W and 0 <= y2 < H and v[y2][x2] == True:
            dfs([y2, x2])


# ユークリッド距離
import numpy

x1 = 2
y1 = 2
x2 = 4
y2 = 6
a = numpy.array([x1, y1])
b = numpy.array([x2, y2])
u = b - a
numpy.linalg.norm(u)

# grid dykstra
def dykstra(y, x):
    dist = []
    for _ in range(H):
        dist.append([INF] * W)
    root = (y, x)
    dist[y][x] = 0
    # ダイクストラ
    Q = [(0, root)]
    while len(Q) > 0:
        d, i = heapq.heappop(Q)
        yi = i[0]
        xi = i[1]
        for yj, xj in [(yi + 1, xi), (yi - 1, xi), (yi, xi + 1), (yi, xi - 1)]:
            if (
                0 <= yj <= H - 1
                and 0 <= xj <= W - 1
                and dist[yj][xj] > dist[yi][xi] + A[yj][xj]
            ):
                dist[yj][xj] = dist[yi][xi] + A[yj][xj]
                heapq.heappush(Q, (dist[yj][xj], (yj, xj)))
    return dist


from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)



# 座標圧縮
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}




# ベルマンフォード
# O(EV)
def bellman_ford(s):
    d = [float("inf")] * V  # 各頂点への最小コスト
    d[s] = 0  # 自身への距離は0
    for i in range(V):
        update = False  # 更新が行われたか
        # すべての辺をたどる
        for s, e, c in G:
            if d[e] > d[s] + c:
                d[e] = d[s] + c
                update = True
        if not update:
            break
        # V-1回以上更新できる場合は負閉路が存在
        if i == V - 1:
            exit(print("inf"))
    return d


V, M = [int(_) for _ in input().split()]
G = []
for _ in range(M):
    s, e, c = [int(x) for x in input().split()]  # 始点,終点,コスト
    # 0はじまりにする
    s -= 1
    e -= 1
    G.append([s, e, c])
    # g.append([e, s, c])  # 無向グラフは逆側もいれる
print(bellman_ford(0))

# 四捨五入
def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

Dis = my_round(Dis / 60, 1)
