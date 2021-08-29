# https://atcoder.jp/contests/typical90/tasks/typical90_aj
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/036.jpg
N = int(input())
X = []
Y = []
xmin = 10 ** 10
xmax = -(10 ** 10)
ymin = 10 ** 10
ymax = -(10 ** 10)
for _ in range(N):
    x, y = [int(_) for _ in input().split()]
    x2 = x + y
    y2 = x - y
    X.append(x2)
    Y.append(y2)
    if x2 > xmax:
        xmax = x2
    if x2 < xmin:
        xmin = x2
    if y2 > ymax:
        ymax = y2
    if y2 < ymin:
        ymin = y2
ans = 0
for i in range(N):
    ans = max(
        ans,
        abs(X[i] - xmax),
        abs(X[i] - xmin),
        abs(Y[i] - ymax),
        abs(Y[i] - ymin),
    )
print(ans)
