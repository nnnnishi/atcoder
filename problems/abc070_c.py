N = int(input())
t = [int(input()) for i in range(N)]

from functools import reduce
import math


def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


# 2つ以上の最小公倍数
print(my_lcm(*t))