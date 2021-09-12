# pythonで提出 !!
import numpy as np

N = int(input())
S = np.array([list(input()) for _ in range(N)])
T = np.array([list(input()) for _ in range(N)])

sy, sx = -1, -1
cnt = 0
m = set()
for y in range(N):
    for x in range(N):
        if S[y][x] == "#":
            cnt += 1
            if sy == -1:
                sy = y
                sx = x
            m.add((y - sy, x - sx))
ccnt = 0
for y in range(N):
    for x in range(N):
        if T[y][x] == "#":
            ccnt += 1

# 数が一致しない
if cnt != ccnt:
    exit(print("No"))

# 4方向に回転させる
for i in range(4):
    T = np.rot90(T)
    check = True
    for y in range(N):
        if check:
            for x in range(N):
                if check and T[y][x] == "#":
                    for dy, dx in m:
                        if (
                            0 <= y + dy < N
                            and 0 <= x + dx < N
                            and T[y + dy][x + dx] == "#"
                        ):
                            continue
                        else:
                            check = False
                    if check:
                        exit(print("Yes"))

print("No")

