N, Q = [int(_) for _ in input().split()]
A = [0] + [int(_) for _ in input().split()]
for i in range(2, N + 1):
    A[i] += A[i - 1]
for i in range(Q):
    l, r = [int(_) for _ in input().split()]
    print(A[r] - A[l - 1])
