N = int(input())
a = [int(_) for _ in input().split()]
b = 0
c = 0
d = 0
for ai in a:
    if ai % 2 != 0:
        b += 1
    else:
        if ai % 4 == 0:
            c += 1
        else:
            d += 1
if d != 0:
    if b > 0 and b > c:
        print("No")
    else:
        print("Yes")
else:
    if b > 0 and b > c + 1:
        print("No")
    else:
        print("Yes")
