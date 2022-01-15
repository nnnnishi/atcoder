N, X, Y = [int(_) for _ in input().split()]
A = [0] * N
A[0] = X
A[1] = Y
for i in range(2, N):
    A[i] = (A[i - 1] + A[i - 2]) % 100
print(A[N - 1])
