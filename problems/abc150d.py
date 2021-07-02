N, M = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
a = list(set(a))
a.sort(reverse=True)

p = 0
# 10**8
ans = 0
for p in range(M // a[0] + 1):
    c = a[0] // 2 + a[0] * p
    if c <= M:
        ok = True
        for ai in a[1:]:
            if ((c / ai) - 1 / 2) != int(((c / ai) - 1 / 2)):
                ok = False
                break
        if ok:
            ans += 1
print(ans)