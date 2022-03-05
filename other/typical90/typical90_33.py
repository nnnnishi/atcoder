s = [int(_) for _ in input().split()]
s.sort()
x, y = s
if x == 1:
    x = -(-x // 2)
    y = y
else:
    x = -(-x // 2)
    y = -(-y // 2)
print(x * y)

