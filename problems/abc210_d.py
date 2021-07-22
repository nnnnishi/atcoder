H, W, C = list(map(int, input().split()))
A = [[int(_) for _ in input().split()] for i in range(H)]


INF = 10 ** 20
dp1 = [[INF] * W for _ in range(H)]
ans1 = [[INF] * W for _ in range(H)]

for y in range(H):
    for x in range(W):
        if not 0 <= x - 1 <= W - 1 and not 0 <= y - 1 <= H - 1:
            dp1[y][x] = A[y][x]
        elif not 0 <= x - 1 <= W - 1:
            dp1[y][x] = min(A[y][x], dp1[y - 1][x] + C)
        elif not 0 <= y - 1 <= H - 1:
            dp1[y][x] = min(A[y][x], dp1[y][x - 1] + C)
        else:
            dp1[y][x] = min(A[y][x], dp1[y][x - 1] + C, dp1[y - 1][x] + C)

for y in range(H):
    for x in range(W):
        if not 0 <= x - 1 <= W - 1 and not 0 <= y - 1 <= H - 1:
            continue
        elif not 0 <= x - 1 <= W - 1:
            ans1[y][x] = dp1[y - 1][x] + A[y][x] + C
        elif not 0 <= y - 1 <= H - 1:
            ans1[y][x] = dp1[y][x - 1] + A[y][x] + C
        else:
            ans1[y][x] = min(dp1[y - 1][x], dp1[y][x - 1]) + A[y][x] + C

Ai = [[0] * H for _ in range(W)]
for y in range(W):
    for x in range(H):
        Ai[y][x] = A[x][(W - 1) - y]

dp2 = [[INF] * H for _ in range(W)]
ans2 = [[INF] * H for _ in range(W)]

for y in range(W):
    for x in range(H):
        if not 0 <= x - 1 <= W - 1 and not 0 <= y - 1 <= H - 1:
            dp2[y][x] = Ai[y][x]
        elif not 0 <= x - 1 <= W - 1:
            dp2[y][x] = min(Ai[y][x], dp2[y - 1][x] + C)
        elif not 0 <= y - 1 <= H - 1:
            dp2[y][x] = min(Ai[y][x], dp2[y][x - 1] + C)
        else:
            dp2[y][x] = min(Ai[y][x], dp2[y][x - 1] + C, dp2[y - 1][x] + C)

for y in range(W):
    for x in range(H):
        if not 0 <= x - 1 <= W - 1 and not 0 <= y - 1 <= H - 1:
            continue
        elif not 0 <= x - 1 <= W - 1:
            ans2[y][x] = dp2[y - 1][x] + Ai[y][x] + C
        elif not 0 <= y - 1 <= H - 1:
            ans2[y][x] = dp2[y][x - 1] + Ai[y][x] + C
        else:
            ans2[y][x] = min(dp2[y - 1][x], dp2[y][x - 1]) + Ai[y][x] + C
# print(ans1)
# print(Ai)
# print(ans2)
ans = INF
for y in range(H):
    for x in range(W):
        ans = min(ans, ans1[y][x], ans2[x][y])
print(ans)