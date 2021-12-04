Y, X = [int(_) for _ in input().split()]
a = [[int(_) for _ in input().split()] for _ in range(Y)]

is_ok = True
for y in range(Y):
    if y == 0:
        for x in range(1, X):
            if a[y][x] != a[y][x - 1] + 1:
                is_ok = False
            if a[y][x] % 7 == 1:
                is_ok = False
    else:
        x = 0
        if X == 7:
            if a[y][x] % 7 != 1:
                is_ok = False
        if a[y][x] != a[y - 1][x] + 7:
            is_ok = False
        for x in range(1, X):
            if a[y][x] != a[y - 1][x] + 7:
                is_ok = False
            if a[y][x] != a[y][x - 1] + 1:
                is_ok = False
            if a[y][x] % 7 == 1:
                is_ok = False
if is_ok:
    print("Yes")
else:
    print("No")

