# https://nashidos.hatenablog.com/entry/2020/06/03/214039
# c**2 = a**2 + b**2 -2*a*b*cos(gamma)
import math

a, b, h, m = [int(_) for _ in input().split()]

# 度数法
long = m * (360 / 60)
short = h * 30 + m * (30 / 60)

# 狭角
if abs(long - short) > 180:
    deg = 360 - abs(long - short)
else:
    deg = abs(long - short)

c = a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(deg))
print(math.sqrt(c))
