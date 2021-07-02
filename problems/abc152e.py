# 2つ以上の最小公約数
from functools import reduce
import math

N = int(input())
A = [int(_) for _ in input().split()]


def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


X = my_lcm(*A)
MOD = 10 ** 9 + 7
X %= MOD
ans = 0
for a in A:
    ans += (X * pow(a, -1, MOD)) % MOD
    ans %= MOD
print(ans)