# 最小公約数: greatest common divisor
# GCDは結合則,交換則が成り立ちどこから計算しても変わらない
# code: https://note.nkmk.me/python-gcd-lcm/
# python 3.9からはmath.gcdで複数もいける
# O(log max(a,b))
import math
from functools import reduce

# 2つ以上の最小公約数
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


A, B, C = [int(_) for _ in input().split()]

d = my_gcd(A, B, C)
print(((A // d) - 1) + ((B // d) - 1) + ((C // d) - 1))
