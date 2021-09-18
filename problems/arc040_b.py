N, R = [int(_) for _ in input().split()]
S = list(input())
cnt = 0
las = 0
for i, s in enumerate(S):
    if s == ".":
        cnt += 1
        las = i

if cnt == 0:
    print(0)
    exit()

if las <= R - 1:
    print(1)
    exit()


ans = 0
for i in range(las - R + 1):
    if S[i] == ".":
        ans += 2
        for j in range(i, i + R):
            S[j] = "o"
    else:
        ans += 1

ans += 1
print(ans)
