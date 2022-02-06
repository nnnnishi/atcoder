N = int(input())
S = list(input())
ans = 0
l = 0
r = N - 1
ok = False
while r > l:
    if S[l] == "W":
        ok = True
        while ok:
            if S[r] == "R":
                ans += 1
                ok = False
            r -= 1
            if l > r:
                break
    l += 1

print(ans)
