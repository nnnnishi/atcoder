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


A, B = [int(_) for _ in input().split()]

l = list(set(prime_factorize(A)) & set(prime_factorize(B)))
l.sort()
if len(l) == 0:
    exit(print(1))
lm = l[-1]
flg = [1] * len(l)
for i in range(len(l)):
    if flg[i]:
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                flg[j] = 0
print(sum(flg) + 1)
