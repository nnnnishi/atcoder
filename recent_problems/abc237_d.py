import numpy as np
import sys

input = sys.stdin.readline

Y, X = list(map(int, input().split()))
A = [[int(_) for _ in input().split()] for _ in range(Y)]

B = np.array(A).T
for i in range(X):
    print(*B[i])
