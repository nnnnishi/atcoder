r, g, b = [int(_) for _ in input().split()]
if int(str(r) + str(g) + str(b)) % 4 == 0:
    print("YES")
else:
    print("NO")