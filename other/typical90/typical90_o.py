N = int(input())
MOD = 10 ** 9 + 7
# nの最大値
LIMIT = 200000

# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bi
# https://github.com/E869120/math-algorithm-book/blob/main/codes/python/Code_5_07_2.py

# 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
def modpow(a, b, m):
    p = a
    answer = 1
    for i in range(30):
        if (b & (1 << i)) != 0:
            answer = (answer * p) % m
        p = (p * p) % m
    return answer


# division(a, b, m) は a÷b mod m を返す関数
def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m


# ncr は n! を r! × (n-r)! で割った値
def ncr(n, r):
    global fact, MOD
    if n <= 0 or r < 0 or n < r:
        return 0
    return division(fact[n], fact[r] * fact[n - r] % MOD, MOD)


# 配列 fact の初期化（fact[i] は i の階乗を 1000000007 で割った余り）
fact = [None] * (LIMIT + 1)
fact[0] = 1
for i in range(1, LIMIT + 1):
    fact[i] = fact[i - 1] * i % MOD

for k in range(1, N + 1):
    ans = 0
    # 平均O(logN)程度
    for i in range(1, N // k + 2):
        s1 = N - (k - 1) * (i - 1)
        s2 = i
        # print(s1, s2, ncr(s1, s2))
        ans += ncr(s1, s2)
        ans %= MOD
    print(ans)
