N = int(input())
A = [0] * (N + 1)
A[1] = 1
if N >= 2:
    A[2] = 2
if N >= 3:
    A[3] = 4
if N >= 4:
    for i in range(4, N + 1):
        A[i] = A[i - 1] + A[i - 2] + A[i - 3]
print(A[N])
