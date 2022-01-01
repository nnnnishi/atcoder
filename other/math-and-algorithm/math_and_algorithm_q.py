# 最小公倍数: least common multiple
# code: https://note.nkmk.me/python-gcd-lcm/
# python 3.9からはmath.lcmがある
from functools import reduce
import math


def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


# 2つ以上の最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


N = int(input())
A = [int(_) for _ in input().split()]
print(my_lcm(*A))
