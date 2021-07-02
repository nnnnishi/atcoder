import math

txa, tya, txb, tyb, T, V = [int(_) for _ in input().split()]
n = int(input())
ok = False
for _ in range(n):
    x, y = [int(_) for _ in input().split()]
    da = math.sqrt((txa - x) ** 2 + (tya - y) ** 2)
    db = math.sqrt((txb - x) ** 2 + (tyb - y) ** 2)
    d = da + db
    if d <= T * V:
        ok = True
if ok:
    print("YES")
else:
    print("NO")
