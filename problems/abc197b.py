H, W, X, Y = list(map(int, input().split()))
S = []
for i in range(H):
    S.append(list(str(input())))

y = X - 1
x = Y - 1
ans = 1
# 上
i = 1
while y - i >= 0:
    if S[y - i][x] == ".":
        ans += 1
        i += 1
    else:
        break
# 下
i = 1
while y + i <= H - 1:
    if S[y + i][x] == ".":
        ans += 1
        i += 1
    else:
        break
# 左
i = 1
while x - i >= 0:
    if S[y][x - i] == ".":
        ans += 1
        i += 1
    else:
        break
# 右
i = 1
while x + i <= W - 1:
    if S[y][x + i] == ".":
        ans += 1
        i += 1
    else:
        break
print(ans)