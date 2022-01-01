import math
from functools import reduce

# 2つ以上の最小公約数
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


N, K = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
ma = max(a)
if K > ma:
    print("IMPOSSIBLE")
else:
    if K % my_gcd(*a) == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

