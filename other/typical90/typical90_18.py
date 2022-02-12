import math

T = int(input())
L, X, Y = [int(_) for _ in input().split()]
Q = int(input())
for _ in range(Q):
    E = int(input())
    theta = 2 * math.pi * ((E / T) % 1)
    y = -(L / 2) * math.sin(theta)
    z = (L / 2) * (1 - math.cos(theta))
    ans = math.degrees(math.atan2(z, math.sqrt(abs(y - Y) ** 2 + X ** 2)))
    print(ans)
