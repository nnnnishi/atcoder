N, M = list(map(int, input().split()))
A = [int(_) for _ in input().split()]

# 素因数分解、試し割り法
# https://qiita.com/drken/items/a14e9af0ca2d857dad23
# O(root(N))
def prime_factorize(n):
    global a
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    # root(N)まで試し割り
    while f * f <= n:
        # 割り切れたらその数で割る
        if n % f == 0:
            a.add(f)
            n //= f
        # 割り切れなかったら偶数はとばして次に行く
        else:
            f += 2
    # のこったものが1でなければそれも約数
    if n != 1:
        a.add(n)
    return


a = set()
is_prime = [0, 0] + [0] * (M - 1)
for ai in A:
    prime_factorize(ai)

for ci in a:
    if ci <= M:
        is_prime[ci] = 1

for n in range(2, M + 1):
    if is_prime[n]:
        check = n + n
        while check < M + 1:
            is_prime[check] = 1
            check += n
print(M - sum(is_prime))
for i in range(1, M + 1):
    if is_prime[i] == 0:
        print(i)
