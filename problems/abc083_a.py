a, b, c, d = [int(_) for _ in input().split()]
x = a + b
y = c + d
if x > y:
    print("Left")
elif x == y:
    print("Balanced")
else:
    print("Right")

