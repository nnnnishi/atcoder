Y, X = [int(_) for _ in input().split()]
A = [list(input()) for _ in range(Y)]

xok = set()
yok = set()
for x in range(X):
    ok = True
    for y in range(Y):
        if A[y][x] == "#":
            ok = False
            break
    if ok:
        xok.add(x)

for y in range(Y):
    ok = True
    for x in range(X):
        if A[y][x] == "#":
            ok = False
            break
    if ok:
        yok.add(y)
for y in range(Y):
    if y not in yok:
        for x in range(X):
            if x not in xok:
                print(A[y][x], end="")
        print("")

