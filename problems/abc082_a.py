a, b = [int(_) for _ in input().split()]
if (a + b) % 2 == 1:
    print((a + b) // 2 + 1)
else:
    print((a + b) // 2)

