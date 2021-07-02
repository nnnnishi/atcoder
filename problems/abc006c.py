N, M = [int(_) for _ in input().split()]
if not 2 * N <= M <= 4 * N:
    exit(print(*[-1, -1, -1]))
res = M - 3 * N
A = 0
B = 0
C = 0
if res < 0:
    A = abs(res)
    B = (M - 2 * A) // 3
else:
    C = res
    B = (M - 4 * C) // 3
print(*[A, B, C])
