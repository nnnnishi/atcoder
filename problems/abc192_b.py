import string

s = set(string.ascii_lowercase)
l = set(string.ascii_uppercase)

S = list(input())
ok = True
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] not in s:
            ok = False
    else:
        if S[i] not in l:
            ok = False
if ok:
    print("Yes")
else:
    print("No")

