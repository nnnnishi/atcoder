N, K = [int(_) for _ in input().split()]
M = 10 ** 9 + 7
if K == 1:
    if N == 1:
        print(1)
    else:
        print(0)
elif K == 2:
    if N <= 2:
        print(2)
    else:
        print(0)
else:
    if N == 1:
        print(K % M)
    elif N == 2:
        print(K * (K - 1) % M)
    else:
        print(K % M * (K - 1) % M * pow(K - 2, N - 2, M) % M)
