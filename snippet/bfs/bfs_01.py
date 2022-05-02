# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/043.jpg
# deque
from collections import deque

Y, X = [int(_) for _ in input().split()]
sy, sx = [int(_) for _ in input().split()]
ty, tx = [int(_) for _ in input().split()]
A = [list(input()) for i in range(Y)]

dist = [[[10 ** 9] * 2 for _ in range(X)] for _ in range(Y)]
# 幅優先
Q = deque()

for i in range(2):
    dist[sy - 1][sx - 1][i] = 0
    Q.append((sy - 1, sx - 1, i))

while Q:
    # 4辺チェックしキューへ追加
    yi, xi, di = Q.popleft()
    c = dist[yi][xi][di]
    for yj, xj, dj in [
        [yi, xi + 1, 0],
        [yi, xi - 1, 0],
        [yi + 1, xi, 1],
        [yi - 1, xi, 1],
    ]:
        if 0 <= yj < Y and 0 <= xj < X and A[yj][xj] == ".":
            if di == dj:
                if dist[yj][xj][dj] > c:
                    dist[yj][xj][dj] = c
                    # 距離0は左から処理する
                    Q.appendleft((yj, xj, dj))
            else:
                if dist[yj][xj][dj] > c + 1:
                    dist[yj][xj][dj] = c + 1
                    Q.append((yj, xj, dj))


print(min(dist[ty - 1][tx - 1]))
