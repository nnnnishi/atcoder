N = int(input())
L = []
R = []

for i in range(N):
    t, l, r = list(map(int, input().split()))
    if t == 1:
        L.append(l)
        R.append(r)
    elif t == 2:
        L.append(l)
        R.append(r - 0.1)
    elif t == 3:
        L.append(l + 0.1)
        R.append(r)
    elif t == 4:
        L.append(l + 0.1)
        R.append(r - 0.1)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if L[i] <= L[j] <= R[i] or L[j] <= L[i] <= R[j]:
            ans += 1
print(ans)
