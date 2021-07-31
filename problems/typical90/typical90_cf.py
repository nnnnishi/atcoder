N = int(input())
S = list(input())
ans = 0
i = 0
j = 0
while i < N - 1:
    if S[i] == "o":
        ini = "o"
    else:
        ini = "x"
    for j in range(i + 1, N):
        if S[j] != ini:
            ans += (j - i) * (N - j)
            break
    i = j
print(ans)