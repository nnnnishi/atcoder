N, K = [int(_) for _ in input().split()]
fill = set()
i2minR = {}
i2maxL = {}
for i in range(K):
    i2minR[i] = N - 1
    i2maxL[i] = 0
for i in range(K):
    c, k = [_ for _ in input().split()]
    k = int(k) - 1
    fill.add(k)
    if c == "L":
        i2maxL[i] = max(k, i2maxL[i])
    else:
        i2minR[i] = min(k, i2minR[i])

ans = 1
for i in range(N):
    if i in fill:
        mut = 1
    else:
        mut = 0
        for j in range(K):
            if i2maxL[j] <= i <= i2minR[j]:
                mut += 1

    if mut > 0:
        ans *= mut
        ans %= 998244353
print(ans)
