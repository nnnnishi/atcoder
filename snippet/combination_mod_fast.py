# https://linus-mk.hatenablog.com/entry/2020/02/23/225258
# nの最大値
n = 10 ** 9
# kの最大値でmodinvテーブルをつくっておく
k = 2 * 10 ** 5
mod = 10 ** 9 + 7

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


print(binomial_coefficients(n, k))