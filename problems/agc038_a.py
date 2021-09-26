import numpy as np

H, W, A, B = [int(_) for _ in input().split()]

a = np.zeros((H, W))
for y in range(H):
    for x in range(W):
        if y < B:
            if x < A:
                a[y][x] = 0
            else:
                a[y][x] = 1
        else:
            if x < A:
                a[y][x] = 1
            else:
                a[y][x] = 0

for y in range(H):
    print("".join(list(map(str, map(int, a[y])))))

