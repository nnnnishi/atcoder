# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/043.jpg
# deque
from collections import deque

Y, X = [int(_) for _ in input().split()]
sy, sx = 0, 0
ty, tx = Y - 1, X - 1
A = [list(input()) for _ in range(Y)]

init = 10 ** 7
dist = [[init] * X for _ in range(Y)]
# 幅優先
Q = deque()


dist[sy][sx] = 0
Q.append((sy, sx))

while dist[ty][tx] == init:
    check = []
    while Q:
        # 4辺チェックしキューへ追加
        yi, xi = Q.popleft()
        check.append((yi, xi))
        c = dist[yi][xi]
        for yj, xj in [[yi, xi + 1], [yi, xi - 1], [yi + 1, xi], [yi - 1, xi]]:
            if 0 <= yj < Y and 0 <= xj < X and A[yj][xj] == ".":
                if dist[yj][xj] > c:
                    dist[yj][xj] = c
                    Q.appendleft((yj, xj))
    # 壁を壊す
    for yi, xi in check:
        flg = 1
        for yj, xj in [
            [yi, xi + 2],
            [yi + 1, xi + 2],
            [yi - 1, xi + 2],
            [yi, xi + 1],
            [yi + 1, xi + 1],
            [yi - 1, xi + 1],
            [yi, xi - 2],
            [yi + 1, xi - 2],
            [yi - 1, xi - 2],
            [yi, xi - 1],
            [yi + 1, xi - 1],
            [yi - 1, xi - 1],
            [yi + 2, xi],
            [yi + 2, xi - 1],
            [yi + 2, xi + 1],
            [yi + 1, xi],
            [yi + 1, xi - 1],
            [yi + 1, xi + 1],
            [yi - 2, xi],
            [yi - 2, xi - 1],
            [yi - 2, xi + 1],
            [yi - 1, xi],
            [yi - 1, xi - 1],
            [yi - 1, xi + 1],
        ]:
            if 0 <= yj < Y and 0 <= xj < X and dist[yj][xj] > c + 1:
                A[yj][xj] = "."
                if flg == 1:
                    dist[yj][xj] = c + 1
                    Q.appendleft((yj, xj))
                    flg = 0
print(dist[ty][tx])