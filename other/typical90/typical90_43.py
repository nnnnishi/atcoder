from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

Y, X = list(map(int, input().split()))

ys, xs = [int(_) for _ in input().split()]
yt, xt = [int(_) for _ in input().split()]
A = [[_ for _ in list(input().rstrip())] for _ in range(Y)]

ans = 0
dist = [[-1] * X for _ in range(Y)]
done = [[False] * X for _ in range(Y)]
xs -= 1
ys -= 1
xt -= 1
yt -= 1
dist[ys][xs] = 0
Q = [[0, ys, xs, 0, 0]]
while len(Q) > 0:
    d, yi, xi, dyi, dxi = heappop(Q)
    if done[yi][xi]:
        continue
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if 0 <= xi + dx < X and 0 <= yi + dy < Y and A[yi + dy][xi + dx] == ".":
            if dyi == dy and dxi == dx:
                if dist[yi + dy][xi + dx] == -1 or dist[yi + dy][xi + dx] > d:
                    dist[yi + dy][xi + dx] = d
                    heappush(Q, (dist[yi + dy][xi + dx], yi + dy, xi + dx, dy, dx))
            else:
                if dist[yi + dy][xi + dx] == -1 or dist[yi + dy][xi + dx] > d + 1:
                    dist[yi + dy][xi + dx] = d + 1
                    heappush(Q, (dist[yi + dy][xi + dx], yi + dy, xi + dx, dy, dx))
        done[yi][xi] = True
print(dist)
print(dist[yt][xt] - 1)
