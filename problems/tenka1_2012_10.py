S = input()
S = S.replace("C", ",C").replace("H", ",H").replace("D", ",D").replace("S", ",S")
s = S.split(",")
# チェック
d = {}
for k in ["S", "C", "H", "D"]:
    d[k] = set()
for i in range(1, len(S)):
    if s[i] in ["SA", "S10", "SQ", "SK", "SJ"]:
        d["S"].add(s[i])
        if len(d["S"]) == 5:
            key = "S"
            break
    if s[i] in ["CA", "C10", "CQ", "CK", "CJ"]:
        d["C"].add(s[i])
        if len(d["C"]) == 5:
            key = "C"
            break
    if s[i] in ["DA", "D10", "DQ", "DK", "DJ"]:
        d["D"].add(s[i])
        if len(d["D"]) == 5:
            key = "D"
            break
    if s[i] in ["HA", "H10", "HQ", "HK", "HJ"]:
        d["H"].add(s[i])
        if len(d["H"]) == 5:
            key = "H"
            break
ans = ""
cnt = 0
for i in range(1, len(S)):
    if s[i] not in d[key]:
        ans += s[i]
    else:
        cnt += 1
        if cnt == 5:
            if ans == "":
                exit(print(0))
            else:
                exit(print(ans))
