Y, X, K = [int(_) for _ in input().split()]
a = [
    [int(_) for _ in list(input().replace("#", "1").replace(".", "0"))]
    for _ in range(Y)
]

b = [[0] * X for i in range(Y)]

tot = 0
for y in range(Y):
    ret = sum(a[y])
    if ret == 0:
        continue
    else:
        tot += 1
        f = True
        for x in range(X):
            if a[y][x] == 0:
                b[y][x] = tot
            elif f and a[y][x] == 1:
                b[y][x] = tot
                f = False
            elif not f and a[y][x] == 1:
                tot += 1
                b[y][x] = tot

# 上から埋める
ok_y = -1
for y in range(Y):
    ret = sum(b[y])
    if ret != 0:
        ok_y = y
    else:
        if ok_y != -1:
            for x in range(X):
                b[y][x] = b[ok_y][x]

# 下から埋める
ok_y = -1
for y in range(Y - 1, -1, -1):
    ret = sum(b[y])
    if ret != 0:
        ok_y = y
    else:
        if ok_y != -1:
            for x in range(X):
                b[y][x] = b[ok_y][x]
for y in range(Y):
    print(*b[y])
