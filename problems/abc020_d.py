from math import gcd

MOD = 10 ** 9 + 7


def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def prime_factorization(n):
    res = []
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.append(i)
    if n != 1:
        res.append(n)
    return res


def f(N, K):
    res = 0
    div = prime_factorization(K)
    # 約数の個数
    M = len(div)
    # 約数（素因数のの組合せの積）について計算
    for bit in range(1 << M):
        mul = 1
        for mask in range(M):
            if bit & (1 << mask):
                mul *= div[mask]
        # 約数の組合せでわる
        d = N // mul
        # 総数を数える
        val = d * (d + 1) % MOD * mul % MOD * pow(2, MOD - 2, MOD) % MOD
        op = -1 if bin(bit).count("1") % 2 else 1
        res += val * op
        res %= MOD
    return res


N, K = map(int, input().split())
gcd_candidate = make_divisors(K)
ans = 0
for g in gcd_candidate:
    ans += K * f(N // g, K // g) % MOD
    ans %= MOD
print(ans)