a, b = list(map(int, input().split()))
if -(-(b - a) // 10) <= 0:
    print(0)
else:
    print(-(-(b - a) // 10))

