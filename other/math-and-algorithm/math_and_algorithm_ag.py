x1, y1, r1 = [int(_) for _ in input().split()]
x2, y2, r2 = [int(_) for _ in input().split()]

dist = (x1 - x2) ** 2 + (y1 - y2) ** 2

# 円が包含される
if abs(r1 - r2) ** 2 > dist:
    print(1)
# 円が包含され接する
elif abs(r1 - r2) ** 2 == dist:
    print(2)
# 円が交差する
elif (r1 + r2) ** 2 > dist:
    print(3)
# 円が外側にあり接する
elif (r1 + r2) ** 2 == dist:
    print(4)
# 円が外側にあり接しない
elif (r1 + r2) ** 2 < dist:
    print(5)
