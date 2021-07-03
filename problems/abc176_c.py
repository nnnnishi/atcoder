H, W = [int(_) for _ in input().split()]
S = [list(input()) for i in range(H)]
ans = 0
for y in range(H - 1):
    for x in range(W - 1):
        cnt = 0
        if S[y][x] == "#":
            cnt += 1
        if S[y + 1][x] == "#":
            cnt += 1
        if S[y][x + 1] == "#":
            cnt += 1
        if S[y + 1][x + 1] == "#":
            cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)