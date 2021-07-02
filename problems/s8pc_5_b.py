import numpy as np

N, M = [int(_) for _ in input().split()]
A = []
B = []
R = []
for i in range(N):
    B.append([int(_) for _ in input().split()])
    R.append(B[i][2])

for i in range(M):
    A.append([int(_) for _ in input().split()])


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


minA = [100] * M
# Aのすべての組み合わせで最小なものをminAとして記録
for i in range(M):
    for j in range(i + 1, M):
        minA[i] = min(dist(A[i][0], A[i][1], A[j][0], A[j][1]) / 2, minA[i])
        minA[j] = min(dist(A[i][0], A[i][1], A[j][0], A[j][1]) / 2, minA[j])
# Bにあてて小さくならないか確認
for i in range(M):
    for j in range(N):
        minA[i] = min(dist(A[i][0], A[i][1], B[j][0], B[j][1]) - B[j][2], minA[i])
print(min(minA + R))
