x, y, d = [_ for _ in input().split()]
x = int(x) - 1
y = int(y) - 1
a = [list(input()) for i in range(9)]
ans = []
if d == "R":
    for i in range(4):
        if x + i < 9:
            ans.append(a[y][x + i])
        else:
            ans.append(a[y][16 - (x + i)])
elif d == "L":
    for i in range(4):
        if x - i >= 0:
            ans.append(a[y][x - i])
        else:
            ans.append(a[y][-(x - i)])
elif d == "D":
    for i in range(4):
        if y + i < 9:
            ans.append(a[y + i][x])
        else:
            ans.append(a[16 - (y + i)][x])
elif d == "U":
    for i in range(4):
        if y - i >= 0:
            ans.append(a[y - i][x])
        else:
            ans.append(a[-(y - i)][x])
elif d == "RD":
    for i in range(4):
        if x + i < 9 and y + i < 9:
            ans.append(a[y + i][x + i])
        elif x + i >= 9 and y + i < 9:
            ans.append(a[y + i][16 - (x + i)])
        elif x + i < 9 and y + i >= 9:
            ans.append(a[16 - (y + i)][x + i])
        else:
            ans.append(a[16 - (y + i)][16 - (x + i)])
elif d == "RU":
    for i in range(4):
        if x + i < 9 and y - i >= 0:
            ans.append(a[y - i][x + i])
        elif x + i >= 9 and y - i >= 0:
            ans.append(a[y - i][16 - (x + i)])
        elif x + i < 9 and y - i < 0:
            ans.append(a[-(y - i)][x + i])
        else:
            ans.append(a[-(y - i)][16 - (x + i)])
elif d == "LD":
    for i in range(4):
        if x - i >= 0 and y + i < 9:
            ans.append(a[y + i][x - i])
        elif x - i < 0 and y + i < 9:
            ans.append(a[y + i][-(x - i)])
        elif x - i >= 0 and y + i >= 9:
            ans.append(a[16 - (y + i)][x - i])
        else:
            ans.append(a[16 - (y + i)][-(x - i)])
elif d == "LU":
    for i in range(4):
        if x - i >= 0 and y - i >= 0:
            ans.append(a[y - i][x - i])
        elif x - i < 0 and y - i >= 0:
            ans.append(a[y - i][-(x - i)])
        elif x - i >= 0 and y - i < 0:
            ans.append(a[-(y - i)][x - i])
        else:
            ans.append(a[-(y - i)][-(x - i)])
print("".join(ans))
