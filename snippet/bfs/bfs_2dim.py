# deque
from collections import deque

Y, X = [int(_) for _ in input().split()]
sy, sx = [int(_) for _ in input().split()]
gy, gx = [int(_) for _ in input().split()]
A = [list(input()) for i in range(Y)]


def bfs():
    # 幅優先
    dist = [[-1] * X for _ in range(Y)]
    Q = deque()
    Q.append([sy - 1, sx - 1])
    dist[sy - 1][sx - 1] = 0
    while len(Q) > 0:
        # 4辺チェックしキューへ追加
        yi, xi = Q.popleft()
        for yj, xj in [[yi, xi + 1], [yi, xi - 1], [yi + 1, xi], [yi - 1, xi]]:
            if 0 <= yj < Y and 0 <= xj < X:
                if A[yj][xj] == "." or A[yj][xj] == "G":
                    if dist[yj][xj] == -1 or dist[yj][xj] > dist[yi][xi] + 1:
                        dist[yj][xj] = dist[yi][xi] + 1
                        Q.append([yj, xj])
    return dist[gy - 1][gx - 1]


print(bfs())
