Y, X = [int(_) for _ in input().split()]
A = []
for i in range(Y):
    S = list(input())
    A.append(S)

M = 998244353
ans = 1
for z in range(X + Y):
    b = 0
    r = 0
    n = 0
    for y in range(Y):
        x = z - y
        if X > x >= 0 and Y > y >= 0:
            if A[y][x] == "B":
                b += 1
            elif A[y][x] == "R":
                r += 1
            else:
                n += 1
    if b > 0 and r > 0:
        exit(print(0))
    else:
        if n > 0 and not (b > 0 or r > 0):
            ans *= 2
            ans %= M
print(ans)
