A, B = [int(_) for _ in input().split()]

# 最小公倍数
import math


def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)


print(my_lcm(A, B))