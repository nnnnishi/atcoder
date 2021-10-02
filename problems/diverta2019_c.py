N = int(input())
ans = 0
a = 0
b = 0
c = 0
for i in range(N):
    S = list(input())
    for j in range(len(S) - 2):
        if S[j] + S[j + 1] == "AB":
            ans += 1

    if S[0] == "B" and S[len(S) - 1] == "A":
        c += 1
    else:
        if S[len(S) - 1] == "A":
            a += 1
        elif S[0] == "B":
            b += 1

if a >= 1:
    ans += c
    ans += min(a, b)
else:
    if c >= 1:
        if b >= 1:
            ans += c
        else:
            ans += c - 1
print(ans)
