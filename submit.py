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


# 座標圧縮
def compress(arr):
    (*XS,) = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}
