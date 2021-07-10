x, y, x1, y1 = [int(_) for _ in input().split()]
x2 = x1 - x
y2 = y1 - y


if x2 >= 0:
    for i in range(x2):
        print("R", end="")
else:
    for i in range(-x2):
        print("L", end="")

if y2 >= 0:
    for i in range(y2):
        print("U", end="")
else:
    for i in range(-x2):
        print("D", end="")

if x2 >= 0:
    for i in range(x2):
        print("L", end="")
else:
    for i in range(-x2):
        print("R", end="")

if y2 >= 0:
    for i in range(y2):
        print("D", end="")
else:
    for i in range(-y2):
        print("U", end="")

if x2 >= 0:
    print("L", end="")
else:
    print("R", end="")

if y2 >= 0:
    print("U", end="")
    for i in range(y2):
        print("U", end="")
else:
    print("D", end="")
    for i in range(-y2):
        print("D", end="")

if x2 >= 0:
    print("R", end="")
    for i in range(x2):
        print("R", end="")
else:
    print("L", end="")
    for i in range(-x2):
        print("L", end="")

if y2 >= 0:
    print("D", end="")
else:
    print("U", end="")

if x2 >= 0:
    print("R", end="")
else:
    print("L", end="")

if y2 >= 0:
    print("D", end="")
    for i in range(y2):
        print("D", end="")
else:
    print("U", end="")
    for i in range(-y2):
        print("U", end="")

if x2 >= 0:
    print("L", end="")
    for i in range(x2):
        print("L", end="")
else:
    print("R", end="")
    for i in range(-x2):
        print("R", end="")

if y2 >= 0:
    print("U")
else:
    print("D")
