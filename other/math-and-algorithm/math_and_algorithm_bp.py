N = int(input())
S = list(input())
s = 0
for i in range(N):
    if S[i] == "(":
        s += 1
    else:
        s -= 1
    if s < 0:
        exit(print("No"))
if s == 0:
    print("Yes")
else:
    print("No")

