# deque
from collections import deque

Y, X, T = 2, 3, 10
A = [["S", "#", "#"], [".", "#", "G"]]


def bfs(t):
    # 幅優先
    dist = [[-1] * X for _ in range(Y)]
    Q = deque()
    Q.append([sy, sx])
    dist[sy][sx] = 0
    while len(Q) > 0:
        # 4辺チェックしキューへ追加
        yi, xi = Q.popleft()
        for yj, xj in [[yi, xi + 1], [yi, xi - 1], [yi + 1, xi], [yi - 1, xi]]:
            if 0 <= yj < Y and 0 <= xj < X:
                if A[yj][xj] == ".":
                    if dist[yj][xj] == -1 or dist[yj][xj] > dist[yi][xi] + 1:
                        dist[yj][xj] = dist[yi][xi] + 1
                        Q.append([yj, xj])
                elif A[yj][xj] == "#":
                    if dist[yj][xj] == -1 or dist[yj][xj] > dist[yi][xi] + t:
                        dist[yj][xj] = dist[yi][xi] + t
                        Q.append([yj, xj])
                elif A[yj][xj] == "G":
                    if dist[yj][xj] == -1 or dist[yj][xj] > dist[yi][xi] + 1:
                        dist[yj][xj] = dist[yi][xi] + 1
    return dist[gy][gx]


for y in range(Y):
    for x in range(X):
        if A[y][x] == "S":
            sx = x
            sy = y
        if A[y][x] == "G":
            gx = x
            gy = y


def meguru_bisect(ok, ng):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if bfs(mid) <= T:
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(-1, 10 ** 9))
