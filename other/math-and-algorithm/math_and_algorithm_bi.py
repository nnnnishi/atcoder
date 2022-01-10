import sys

# https://linus-mk.hatenablog.com/entry/2020/02/23/225258
# nの最大値
# kの最大値でmodinvテーブルをつくっておく
k = 2 * 10 ** 5
mod = 10 ** 9 + 7

modinv_table = [-1] * (k + 1)
modinv_table[1] = 1
for i in range(2, k + 1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod


def binomial_coefficients(n, k):
    d = {}
    ans = 1
    d[0] = ans
    for i in range(k):
        ans *= n - i
        ans *= modinv_table[i + 1]
        ans %= mod
        d[i + 1] = ans
    return d


input = sys.stdin.readline
N = int(input())
A = [int(_) for _ in input().split()]
ans = 0
d = binomial_coefficients(N - 1, (N - 1) // 2 + 1)
for k in range(N):
    if N - 1 - k < k:
        break
    # print(binomial_coefficients(N - 1, k), A[k], A[N - 1 - k])
    if k != N - 1 - k:
        ans += (A[k] + A[N - 1 - k]) * d[k] % mod
        ans %= mod
    else:
        ans += A[k] * d[k] % mod
        ans %= mod

print(ans)
