a, b, c = [int(_) for _ in input().split()]
if a == 1:
    if c == 1:
        print("No")
    else:
        print("Yes")
else:
    if a < pow(c, b):
        print("Yes")
    else:
        print("No")

