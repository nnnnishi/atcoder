from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

# grid dykstra
N = int(input())
H, W = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for i in range(N)]
INF = 10 ** 20


def dykstra(y, x):
    dist = []
    for _ in range(H):
        dist.append([INF] * W)
    root = (y, x)
    dist[y][x] = 0
    # ダイクストラ
    Q = [(0, root)]
    while len(Q) > 0:
        d, i = heappop(Q)
        yi = i[0]
        xi = i[1]
        for yj, xj in [(yi + 1, xi), (yi - 1, xi), (yi, xi + 1), (yi, xi - 1)]:
            if (
                0 <= yj <= H - 1
                and 0 <= xj <= W - 1
                and dist[yj][xj] > dist[yi][xi] + A[yj][xj]
            ):
                dist[yj][xj] = dist[yi][xi] + A[yj][xj]
                heappush(Q, (dist[yj][xj], (yj, xj)))
    return dist