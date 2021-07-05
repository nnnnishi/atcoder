# GCDは結合則が成り立ちどこから計算しても変わらない
# abc125_c: https://img.atcoder.jp/abc125/editorial.pdf
# code: https://qiita.com/derodero24/items/91b6468e66923a87f39f

# Nが大きい
def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result


# Nが小さい
def cmb_sml(n, r):
    nCr = {}
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    if (n, r) in nCr:
        return nCr[(n, r)]
    nCr[(n, r)] = cmb(n - 1, r) + cmb(n - 1, r - 1)
    return nCr[(n, r)]


# MODがはいる
def cmb_mod(n, r, mod):
    r = min(r, n - r)
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル

    for i in range(2, n + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    if r < 0 or r > n:
        return 0

    return g1[n] * g2[r] * g2[n - r] % mod


MOD = 10 ** 9 + 7
print(cmb(10000, 3))
print(cmb_sml(10000, 3))
print(cmb_mod(10000, 3, MOD))
print(166616670000 % MOD)
