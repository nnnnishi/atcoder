Y, X = [int(_) for _ in input().split()]

A = [list(input()) for i in range(Y)]
a = set()
# もどす
for y in range(Y):
    for x in range(X):
        if A[y][x] == "#":
            find = True
            for xdif in [-1, 0, 1]:
                for ydif in [-1, 0, 1]:
                    if 0 <= x + xdif < X and 0 <= y + ydif < Y:
                        if A[y + ydif][x + xdif] != "#":
                            find = False
            if find:
                a.add((y, x))

B = [["."] * X for i in range(Y)]
for y in range(Y):
    for x in range(X):
        if (y, x) in a:
            for xdif in [-1, 0, 1]:
                for ydif in [-1, 0, 1]:
                    if 0 <= x + xdif < X and 0 <= y + ydif < Y:
                        B[y + ydif][x + xdif] = "#"

for y in range(Y):
    for x in range(X):
        if A[y][x] != B[y][x]:
            exit(print("impossible"))

print("possible")
B = [["."] * X for i in range(Y)]
for y in range(Y):
    for x in range(X):
        if (y, x) in a:
            B[y][x] = "#"
    print("".join(B[y]))
