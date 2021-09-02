N = int(input())
X = []
Y = []
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

ans = 0
if N % 2 != 0:
    cx, cy = (X[N // 2], Y[N // 2])
    for i in range(N):
        ans += abs(cx - X[i]) + abs(cy - Y[i])
else:
    ans1 = 0
    cx, cy = (X[N // 2], Y[N // 2])
    for i in range(N):
        ans1 += abs(cx - X[i]) + abs(cy - Y[i])
    ans2 = 0
    cx, cy = (X[N // 2 - 1], Y[N // 2 - 1])
    for i in range(N):
        ans2 += abs(cx - X[i]) + abs(cy - Y[i])
    ans = min(ans1, ans2)
print(ans)