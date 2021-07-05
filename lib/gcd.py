# 最小公約数: greatest common divisor
# GCDは結合則,交換則が成り立ちどこから計算しても変わらない
# code: https://note.nkmk.me/python-gcd-lcm/
# python 3.9からはmath.gcdで複数もいける

import math
from functools import reduce

# 2つ以上の最小公約数
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


print(math.gcd(4, 6))
print(my_gcd(4, 6, 8))
print(my_gcd(*[4, 6, 8]))