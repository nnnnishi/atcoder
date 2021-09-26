S = list(input())
N = len(S)
a = ""
for i in range(N):
    if S[i] != "x":
        a += S[i]
b = ""
for i in range(N):
    if S[N - i - 1] != "x":
        b += S[N - i - 1]
if a != b:
    exit(print(-1))

j = N - 1
i = 0
ans = 0
while i < j:
    if S[i] == "x" and S[j] == "x":
        i += 1
        j -= 1
    elif S[i] != "x" and S[j] == "x":
        while S[j] == "x":
            ans += 1
            j -= 1
    elif S[i] == "x" and S[j] != "x":
        while S[i] == "x":
            ans += 1
            i += 1
    elif S[i] != "x" and S[j] != "x":
        i += 1
        j -= 1
print(ans)
