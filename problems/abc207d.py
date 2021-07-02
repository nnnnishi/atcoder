import math

N = int(input())
if N == 1:
    exit(print("Yes"))

S = []
T = []
sx = 0
sy = 0
tx = 0
ty = 0
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    S.append([x * N, y * N])
    sx += x * N
    sy += y * N
sx //= N
sy //= N
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    T.append([x * N, y * N])
    tx += x * N
    ty += y * N
tx //= N
ty //= N


S1 = []
T1 = []
allzero = True
for x, y in S:
    r = (x - sx) ** 2 + (y - sy) ** 2

    d = math.degrees(math.atan2(x - sx, y - sy))
    if d < 0:
        d += 360
    elif d >= 360:
        d -= 360
    S1.append([r, d])
    if r > 0:
        allzero = False
if allzero:
    exit(print("Yes"))

for x, y in T:
    r = (x - tx) ** 2 + (y - ty) ** 2

    d = math.degrees(math.atan2(x - tx, y - ty))
    if d < 0:
        d += 360
    elif d >= 360:
        d -= 360
    T1.append([r, d])


# S1のr!=0の点について、回転させて一致するものを確認
for s in S1:
    if s[0] != 0:
        sr = s[0]
        sd = s[1]
# dd -> sdにたすとtdになる
cand_dd = []
for t in T1:
    if t[0] == sr:
        # print(t[0], sr)
        cand_dd.append(t[1] - sd)

# print(cand_dd)

for dd in cand_dd:
    # print(dd, "d")
    ok = False
    cnt = 0
    for s in S1:
        # 原点と重心が一致するものは除外
        if s[0] == 0:
            for t in T1:
                if t[0] == 0:
                    cnt += 1
                    break
        else:
            sd = s[1] + dd
            if sd < 0:
                sd += 360
            elif sd >= 360:
                sd -= 360
            for t in T1:
                if s[0] == t[0]:
                    # print(sd, t[1])
                    if abs(sd - t[1]) <= 0.00001:
                        cnt += 1
                        break
    # print(cnt)
    if cnt >= N:
        exit(print("Yes"))

print("No")
