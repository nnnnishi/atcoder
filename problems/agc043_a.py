# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/043.jpg
# deque
from collections import deque

Y, X = [int(_) for _ in input().split()]
sy, sx = 1, 1
ty, tx = Y, X
A = [list(input()) for i in range(Y)]

dist = [[10 ** 9] * X for _ in range(Y)]
# 幅優先
Q = deque()
R = deque()
if A[sy - 1][sy - 1] == ".":
    dist[sy - 1][sx - 1] = 0
    Q.append((sy - 1, sx - 1))
else:
    dist[sy - 1][sx - 1] = 1
    R.append((sy - 1, sx - 1))


# 白チェック
while True:
    while Q:
        # 4辺チェックしキューへ追加
        yi, xi = Q.popleft()
        c = dist[yi][xi]
        for yj, xj in [[yi, xi + 1], [yi + 1, xi]]:
            if 0 <= yj < Y and 0 <= xj < X:
                if A[yj][xj] == ".":
                    if dist[yj][xj] > c:
                        dist[yj][xj] = c
                        Q.appendleft((yj, xj))
                else:
                    if dist[yj][xj] > c + 1:
                        dist[yj][xj] = c + 1
                        R.appendleft((yj, xj))
        if dist[ty - 1][tx - 1] != 10 ** 9:
            exit(print(dist[ty - 1][tx - 1]))

    # 黒チェック
    while R:
        # 4辺チェックしキューへ追加
        yi, xi = R.popleft()
        c = dist[yi][xi]
        for yj, xj in [[yi, xi + 1], [yi + 1, xi]]:
            if 0 <= yj < Y and 0 <= xj < X:
                if A[yj][xj] == ".":
                    if dist[yj][xj] > c:
                        dist[yj][xj] = c
                        Q.appendleft((yj, xj))
                else:
                    if dist[yj][xj] > c:
                        dist[yj][xj] = c
                        R.appendleft((yj, xj))
        if dist[ty - 1][tx - 1] != 10 ** 9:
            exit(print(dist[ty - 1][tx - 1]))

