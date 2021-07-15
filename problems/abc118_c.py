N = int(input())
A = [int(_) for _ in input().split()]


import math
from functools import reduce

# 2つ以上の最小公約数
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


print(my_gcd(*A))