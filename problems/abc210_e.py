import math
from functools import reduce

# 2つ以上の最小公約数
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


N, M = [int(_) for _ in input().split()]
A = []
C = []
P = []
for i in range(M):
    a, c = [int(_) for _ in input().split()]
    A.append(a)
    C.append(c)
    P.append((c, a))
P.sort()

# 公約数が1でなければだめ
if my_gcd(*([N] + A)) != 1:
    exit(print(-1))
# NとaのGCDをかくにんし、1ならそれでいく
ans = 0
group = N
g = N
for p in P:
    c, a = p
    g = my_gcd(g, a)
    if g == 1:
        ans += (group - 1) * c
        exit(print(ans))
    else:
        if g < group:
            ans += (group - g) * c
            group = g
