H, W = list(map(int, input().split()))
A = []
for i in range(H):
    A.append([int(_) for _ in input().split()])

for i1 in range(H):
    for i2 in range(i1 + 1, H):
        for j1 in range(W):
            for j2 in range(j1 + 1, W):
                if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                    exit(print("No"))
print("Yes")

