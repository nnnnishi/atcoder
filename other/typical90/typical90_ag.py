x, y = [int(_) for _ in input().split()]
if x == 1 or y == 1:
    print(x * y)
else:
    print(-(-x // 2) * -(-y // 2))
