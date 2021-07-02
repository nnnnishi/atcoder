S = list(input())
rS = S[::-1]
ans = []
for s in rS:
    if s == "0":
        ans.append("0")
    elif s == "1":
        ans.append("1")
    elif s == "6":
        ans.append("9")
    elif s == "8":
        ans.append("8")
    elif s == "9":
        ans.append("6")
print("".join(ans))