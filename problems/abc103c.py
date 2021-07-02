import math

# 2つ以上の最小公約数
from functools import reduce

N = int(input())
A = [int(_) for _ in input().split()]

# 2つ以上の最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


S = my_lcm(*A) - 1
ans = 0
for a in A:
    ans += S % a
print(ans)
