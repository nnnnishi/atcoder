N = int(input())
S = list(input())
ans = 0
for i in range(N):
    if S[i] != ".":
        ans += 1

tmp = ans

for i in range(N - 1, -1, -1):
    if S[i] == "#":
        tmp -= 1
    else:
        tmp += 1
    ans = min(tmp, ans)
print(ans)
