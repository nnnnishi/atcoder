from functools import reduce
import math

N = int(input())
A = [int(_) for _ in input().split()]


def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


print(my_gcd(*A))