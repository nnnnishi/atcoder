from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

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


N, P = [int(_) for _ in input().split()]

L = prime_factorize(P)
d = Counter(L)

ans = 1
for k, v in d.items():
    if v // N > 0:
        ans *= k ** (v // N)
print(ans)

