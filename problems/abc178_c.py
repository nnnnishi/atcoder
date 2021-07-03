N = int(input())
MOD = 10 ** 9 + 7
if N == 1:
    exit(print(0))
a = pow(10, N, MOD) - 2 * pow(9, N, MOD) + pow(8, N, MOD)
print(a % MOD)
