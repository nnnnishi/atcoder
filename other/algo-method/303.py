N = int(input())
A = [int(_) for _ in input().split()]
T = [0] * N
T[1] = A[1]
for i in range(2, N):
    T[i] = min(T[i - 2] + 2 * A[i], T[i - 1] + A[i])
print(T[N - 1])

