# https://linus-mk.hatenablog.com/entry/2020/02/23/225258
# nの最大値
# kの最大値でmodinvテーブルをつくっておく
mod = 10 ** 9 + 7
k = 10 ** 6
modinv_table = [-1] * (k + 1)
modinv_table[1] = 1
for i in range(2, k + 1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod


def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans


X, Y = [int(_) for _ in input().split()]
if (2 * X - Y) % 3 == 0 and (-X + 2 * Y) % 3 == 0:
    a = (2 * X - Y) // 3
    b = (-X + 2 * Y) // 3
    print(binomial_coefficients(a + b, max(a, b)))
else:
    print(0)
