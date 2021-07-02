N = int(input())
a = [int(_) for _ in input().split()]
INF = 0
A = [INF] * N
A[0] = 0
A[1] = abs(a[1] - a[0])
if N == 2:
    exit(print(A[1]))
for i in range(2, N):
    A[i] = min(A[i - 1] + abs(a[i] - a[i - 1]), A[i - 2] + abs(a[i] - a[i - 2]))

print(A[N - 1])
