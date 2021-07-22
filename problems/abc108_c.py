N, K = [int(_) for _ in input().split()]

a = 0
b = 0
if K % 2 == 0:
    for i in range(1, N + 1):
        if i % K == 0:
            a += 1
        if i % K == (K // 2):
            b += 1
    print(a ** 3 + b ** 3)
else:
    for i in range(1, N + 1):
        if i % K == 0:
            a += 1
    print(a ** 3)
