# 素因数分解、試し割り法
# https://qiita.com/drken/items/a14e9af0ca2d857dad23
# O(root(N))
# 約数列挙
def make_divisors(N):
    div_low = []
    div_high = []
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i == 0:
            div_low.append(i)
            if i != N // i:
                div_high.append(N // i)

    div = div_low + div_high[::-1]
    return div


N = int(input())
for i in make_divisors(N):
    print(i)
