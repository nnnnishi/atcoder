import math
from functools import reduce


# 2つ以上の最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


n, x, y = [int(_) for _ in input().split()]
print((n // x) + (n // y) - (n // my_lcm_base(x, y)))
