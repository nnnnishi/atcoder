N, Q = [int(_) for _ in input().split()]
X = []
Y = []
xmin = 10 ** 10
xmax = -(10 ** 10)
ymin = 10 ** 10
ymax = -(10 ** 10)
for _ in range(N):
    x, y = [int(_) for _ in input().split()]
    x2 = x + y
    y2 = x - y
    X.append(x2)
    Y.append(y2)
    if x2 > xmax:
        xmax = x2
    if x2 < xmin:
        xmin = x2
    if y2 > ymax:
        ymax = y2
    if y2 < ymin:
        ymin = y2

for _ in range(Q):
    q = int(input())
    print(
        max(
            abs(X[q - 1] - xmax),
            abs(X[q - 1] - xmin),
            abs(Y[q - 1] - ymax),
            abs(Y[q - 1] - ymin),
        )
    )
