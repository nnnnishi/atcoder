import math

a, b, n = [int(_) for _ in input().split()]
ans = 0
if n > b - 1:
    i = b - 1
else:
    i = n
t = math.floor(a * i / b) - a * math.floor(i / b)
print(t)
