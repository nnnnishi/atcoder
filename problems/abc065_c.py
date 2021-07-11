a, b = [int(_) for _ in input().split()]
if abs(a - b) > 1:
    exit(print(0))
MOD = 10 ** 9 + 7
if (a + b) % 2 == 0:
    tmp = 1
    for i in range(1, a + 1):
        tmp *= i
        tmp = tmp % MOD
    print((tmp * tmp * 2) % MOD)
else:
    tmp = 1
    mi = min(a, b)
    ma = max(a, b)
    for i in range(1, mi + 1):
        tmp *= i
        tmp = tmp % MOD
    print((tmp * tmp * ma) % MOD)