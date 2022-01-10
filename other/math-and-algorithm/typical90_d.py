import sys

input = sys.stdin.readline

Y, X = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for _ in range(Y)]

YL = [0] * Y
XL = [0] * X

for i in range(Y):
    for j in range(X):
        YL[i] += A[i][j]
        XL[j] += A[i][j]

for i in range(Y):
    for j in range(X):
        A[i][j] = YL[i] + XL[j] - A[i][j]

for i in range(Y):
    print(*A[i])
