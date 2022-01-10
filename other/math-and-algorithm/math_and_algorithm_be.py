import sys
import math
from functools import reduce

# 2つ以上の最小公約数
def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


# 2つ以上の最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


input = sys.stdin.readline

N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
def has_bit(n, i):
    return (n & 1 << i) > 0


ans = 0
# N桁の0-1の組合せパターン数 1<<N
for n in range(1, 1 << K):
    # 要素数
    L = []
    for i in range(K):
        # パターンnのi桁目が1
        if has_bit(n, i):
            L.append(A[i])
    # print(L)
    if len(L) % 2 == 0:
        ans -= N // my_lcm(*L)
    else:
        ans += N // my_lcm(*L)
print(ans)
