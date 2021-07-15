N, X = [int(_) for _ in input().split()]
x = [int(_) for _ in input().split()]
x.append(X)
x.sort()
dif = set()
for i in range(N):
    dif.add(x[i + 1] - x[i])
dif = list(dif)

import math
from functools import reduce

# 2つ以上の最小公約数
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


print(my_gcd(*dif))