N = int(input())

# 素因数分解、試し割り法
# https://qiita.com/drken/items/a14e9af0ca2d857dad23
# O(root(N))
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    # root(N)まで試し割り
    while f * f <= n:
        # 割り切れたらその数で割る
        if n % f == 0:
            a.append(f)
            n //= f
        # 割り切れなかったら偶数はとばして次に行く
        else:
            f += 2
    # のこったものが1でなければそれも約数
    if n != 1:
        a.append(n)
    return a


if len(prime_factorize(N)) == 1:
    print(0)
else:
    c = len(prime_factorize(N))
    a = 0
    while c > 1:
        c = -(-c // 2)
        a += 1
    print(a)
