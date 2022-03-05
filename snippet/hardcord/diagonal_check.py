import sys

input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    S = input().rstrip().replace(".", "0").replace("#", "1")
    S = list(map(int, S))
    A.append(S)

# よこ
for y in range(N):
    for x in range(N):
        res = 2
        cnt = 0
        for t in range(6):
            if x + t < N:
                if A[y][x + t] == 0:
                    res -= 1
                    cnt += 1
                    if res < 0:
                        break
                    if cnt == 6:
                        print("Yes")
                        exit()

                else:
                    cnt += 1
                    if cnt == 6:
                        print("Yes")
                        exit()
            else:
                break

# たて
for y in range(N):
    for x in range(N):
        res = 2
        cnt = 0
        for t in range(6):
            if y + t < N:
                if A[y + t][x] == 0:
                    res -= 1
                    cnt += 1
                    if res < 0:
                        break
                    if cnt == 6:
                        print("Yes")
                        exit()

                else:
                    cnt += 1
                    if cnt == 6:
                        print("Yes")
                        exit()
            else:
                break

# みぎした
for y in range(N):
    for x in range(N):
        res = 2
        cnt = 0
        for t in range(6):
            if x + t < N and y + t < N:
                if A[y + t][x + t] == 0:
                    res -= 1
                    cnt += 1
                    if res < 0:
                        break
                    if cnt == 6:
                        print("Yes")
                        exit()

                else:
                    cnt += 1
                    if cnt == 6:
                        print("Yes")
                        exit()
            else:
                break

# ひだりした
for y in range(N):
    for x in range(N):
        res = 2
        cnt = 0
        for t in range(6):
            if y + t < N and x - t >= 0:
                if A[y + t][x - t] == 0:
                    res -= 1
                    cnt += 1
                    if res < 0:
                        break
                    if cnt == 6:
                        print("Yes")
                        exit()

                else:
                    cnt += 1
                    if cnt == 6:
                        print("Yes")
                        exit()
            else:
                break

print("No")
