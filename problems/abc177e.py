# 2つ以上の最小公約数
import math
from functools import reduce


def my_gcd(numbers):
    return reduce(math.gcd, numbers)


N = int(input())
A = [int(_) for _ in input().split()]
if my_gcd(A) != 1:
    exit(print("not coprime"))


# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


Amax = max(A)
num = [0] * (Amax + 1)
for a in A:
    for i in list(set(prime_factorize(a))):
        num[i] += 1
        if num[i] > 1:
            exit(print("setwise coprime"))
print("pairwise coprime")
