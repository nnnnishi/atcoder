S = input()
if (
    S[:-7] == "keyence"
    or (S[:1] == "k" and S[-6:] == "eyence")
    or (S[:2] == "ke" and S[-5:] == "yence")
    or (S[:3] == "key" and S[-4:] == "ence")
    or (S[:4] == "keye" and S[-3:] == "nce")
    or (S[:5] == "keyen" and S[-2:] == "ce")
    or (S[:6] == "keyenc" and S[-1:] == "e")
    or S[:7] == "keyence"
):
    print("YES")
else:
    print("NO")

