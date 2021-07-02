N = int(input())
S = list(input())
ans = 1
for i in range(1, N):
    if S[i] != S[i - 1]:
        ans += 1
print(ans)