H, W = [int(_) for _ in input().split()]
S = []
for i in range(H):
    S.append(list(input()))
K = 0

hori = []
for y in range(H):
    cnt = 0
    fil = 0
    hori.append([])
    for x in range(W):
        if S[y][x] == ".":
            cnt += 1
        else:
            for x1 in range(fil, x):
                hori[y].append(cnt)
            cnt = 0
            hori[y].append(cnt)
            fil = x + 1
    for x1 in range(fil, x + 1):
        hori[y].append(cnt)

ver = []
K = 0
for x in range(W):
    cnt = 0
    fil = 0
    ver.append([])
    for y in range(H):
        if S[y][x] == ".":
            cnt += 1
            K += 1
        else:
            for y1 in range(fil, y):
                ver[x].append(cnt)
            cnt = 0
            ver[x].append(cnt)
            fil = y + 1
    for y1 in range(fil, y + 1):
        ver[x].append(cnt)
ans = 0
M = 10 ** 9 + 7

# 2^Kまでを事前計算
pow2 = [1] * (K + 1)
for i in range(1, K + 1):
    pow2[i] = pow2[i - 1] * 2 % M

for x in range(W):
    for y in range(H):
        if S[y][x] == ".":
            ans += (pow2[K] - pow2[K - (ver[x][y] + hori[y][x] - 1)]) % M
            ans %= M
print(ans)