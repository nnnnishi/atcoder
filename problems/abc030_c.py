N, M = [int(_) for _ in input().split()]
X, Y = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
t = 0
ix = 0
jx = 0
ans = 0
while ix < N or jx < M:
    ok = False
    while ix < N:
        if a[ix] >= t:
            t = a[ix] + X
            ok = True
            break
        else:
            ix += 1
    if not ok:
        break
    while jx < M:
        if b[jx] >= t:
            t = b[jx] + Y
            ans += 1
            break
        else:
            jx += 1
print(ans)