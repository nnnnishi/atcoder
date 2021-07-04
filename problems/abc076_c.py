S = list(input())
T = list(input())
lt = len(T)
ls = len(S)
ans = ""
for i in range(ls - lt, -1, -1):
    cnt = 0
    ok = True
    for j in range(lt):
        # print(S[i + cnt], T[j])
        if S[i + cnt] != "?" and S[i + cnt] != T[j]:
            ok = False
        cnt += 1
    if ok:
        # print(i, "i")
        cnt = 0
        for i2 in range(ls):
            if i2 < i or i2 > i + lt - 1:
                if S[i2] != "?":
                    ans += S[i2]
                else:
                    ans += "a"
            else:
                ans += T[cnt]
                cnt += 1
        exit(print(ans))
print("UNRESTORABLE")
