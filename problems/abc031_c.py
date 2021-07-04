N = int(input())
A = [int(_) for _ in input().split()]
ans = -(10 ** 10)
for t in range(N):
    apmax = -(10 ** 10)
    tpmax = -(10 ** 10)
    for a in range(N):
        if a != t:
            ap = 0
            tp = 0
            l = min(a, t)
            r = max(a, t)
            for i in range(l, r + 1):
                if (i - l) % 2 != 0:
                    ap += A[i]
                else:
                    tp += A[i]
            if ap > apmax:
                apmax = ap
                tpmax = tp
    if ans <= tpmax:
        # print(t, a)
        ans = max(ans, tpmax)
print(ans)
