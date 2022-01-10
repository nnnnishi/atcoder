import math

a, b = [int(_) for _ in input().split()]

c = math.gcd(a, b)
if a * b // c > 10 ** 18:
    print("Large")
else:
    print(a * b // c)

