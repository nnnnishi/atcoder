N = int(input())
A = []
A.append([int(_) for _ in input().split()])
for i in range(N - 1):
    A.append([0] * N)

for i in range(1, N):
    for j in range(N):
        for k in range(-1, 2):
            if 0 <= j + k <= N - 1:
                A[i][j] += A[i - 1][j + k]
                A[i][j] %= 100
print(A[N - 1][N - 1])

