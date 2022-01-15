N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
T = [10 ** 10] * (N)
T[0] = 0
for i in range(1, N):
    for j in range(1, M + 1):
        if i - j >= 0:
            T[i] = min(T[i], T[i - j] + j * A[i])
print(T[-1])
