S = input()
S2 = ""
b = ""
# スペースけす
for s in list(S):
    if b == " " and s == " ":
        continue
    S2 += s
    b = s
# カンマ置換
print(S2.replace(" ", ","))
