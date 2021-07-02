W, H, x, y = [int(_) for _ in input().split()]
s = W * H
if x * 2 == W and y * 2 == H:
    flg = 1
else:
    flg = 0

print(s / 2, flg)
