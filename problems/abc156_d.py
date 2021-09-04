# abc125_c: https://img.atcoder.jp/abc125/editorial.pdf
# code: https://qiita.com/derodero24/items/91b6468e66923a87f39f


def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans


N, A, B = [int(_) for _ in input().split()]

# kの最大値
k = max(min(A, 10 ** 9 - A), min(B, 10 ** 9 - B))
mod = 10 ** 9 + 7

modinv_table = [-1] * (k + 1)
modinv_table[1] = 1
for i in range(2, k + 1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod


s = pow(2, N, mod)
a = binomial_coefficients(N, A)
b = binomial_coefficients(N, B)
print((s - (a % mod) - (b % mod) - 1) % mod)
