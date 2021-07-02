W, H, N = [int(_) for _ in input().split()]
upper = H
lower = 0
right = W
left = 0
white = []
for i in range(H):
    white.append([1] * W)

for i in range(N):
    xi, yi, ai = [int(_) for _ in input().split()]
    if ai == 1:  # 左側
        for y in range(H):
            for x in range(xi):
                white[y][x] = 0
    elif ai == 2:
        for y in range(H):
            for x in range(xi, W):
                white[y][x] = 0
    elif ai == 3:
        for y in range(yi):
            for x in range(W):
                white[y][x] = 0
    elif ai == 4:
        for y in range(yi, H):
            for x in range(W):
                white[y][x] = 0
ans = 0
for y in range(H):
    ans += sum(white[y])
print(ans)
