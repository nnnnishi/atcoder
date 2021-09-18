# pythonで提出 !!
import numpy as np

N, M = [int(_) for _ in input().split()]
S = np.array([list(input()) for _ in range(N)])
T = np.array([list(input()) for _ in range(M)])

for y1 in range(N - M + 1):
    for x1 in range(N - M + 1):
        ok = True
        for y2 in range(M):
            if ok:
                for x2 in range(M):
                    if T[y2][x2] != S[y1 + y2][x1 + x2]:
                        ok = False
                        break
        if ok:
            exit(print("Yes"))
print("No")

