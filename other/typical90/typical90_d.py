Y, X = [int(_) for _ in input().split()]
a = []
for i in range(Y):
    a.append([int(_) for _ in input().split()])

sy = []
sx = [0] * X
for i in range(Y):
    sy.append(sum(a[i]))
    for j in range(X):
        sx[j] += a[i][j]

for i in range(Y):
    t = []
    for j in range(X):
        t.append(sy[i] + sx[j] - a[i][j])
    print(*t)