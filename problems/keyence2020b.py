N = int(input())
X = []
L = []
XL = []
for i in range(N):
    x, l = [int(_) for _ in input().split()]
    X.append(x)
    L.append(l)
    XL.append([x + l, x - l])
XL.sort()

ans = 1
d = XL[0][0]
for xl in XL[1:]:
    if d <= xl[1]:
        ans += 1
        d = xl[0]
print(ans)