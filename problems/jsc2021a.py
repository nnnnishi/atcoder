X, Y, Z = list(map(int, input().split()))
if (Y * Z / X) - ((Y * Z / X) // 1) != 0:
    print(int((Y * Z / X) // 1))
else:
    print(int((Y * Z / X) // 1) - 1)
