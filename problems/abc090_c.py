N, M = [int(_) for _ in input().split()]
if N == M == 1:
    print(1)
elif N == 1 and M >= 2:
    print(M - 2)
elif N >= 2 and M == 1:
    print(N - 2)
else:
    print((N - 2) * (M - 2))
