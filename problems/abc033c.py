S = list(input())
ans = 0
tmp = 0
z_exist = 0
for i in range(len(S)):
    # 数字
    if i % 2 == 0:
        if S[i] != "0" and z_exist != 1:
            tmp = 1
        else:
            tmp = 0
            z_exist = 1
    else:
        if S[i] == "+":
            if tmp == 1:
                ans += 1
            tmp = 0
            z_exist = 0
if tmp == 1:
    ans += 1
print(ans)