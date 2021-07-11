import math


# 2つ以上の最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


a, b, c, d = [int(_) for _ in input().split()]
all = b - a + 1

t1 = (b // c) - ((a - 1) // c)
t2 = (b // d) - ((a - 1) // d)
t3 = (b // my_lcm_base(c, d)) - ((a - 1) // my_lcm_base(c, d))
print(all - (t1 + t2 - t3))
