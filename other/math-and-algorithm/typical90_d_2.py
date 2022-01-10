import sys
import numpy as np

input = sys.stdin.readline


Y, X = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for _ in range(Y)]
B = [[0] * X for _ in range(Y)]
YL = [0] * Y
XL = [0] * X

for i in range(Y):
    YL[i] = sum(A[i])

C = np.array(A).T.tolist()
for i in range(X):
    XL[i] = sum(C[i])

for i in range(Y):
    for j in range(X):
        B[i][j] = YL[i] + XL[j] - A[i][j]

for i in range(Y):
    print(*B[i])
