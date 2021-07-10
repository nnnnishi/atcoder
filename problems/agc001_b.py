N, X = [int(_) for _ in input().split()]

import math
from functools import reduce

print(3 * (N - math.gcd(N, X)))
