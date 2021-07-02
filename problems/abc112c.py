import itertools

N = int(input())
x = []
y = []
h = []
for _ in range(N):
    x1, y1, h1 = list(map(int, input().split()))
    if h1 != 0:
        x.append(x1)
        y.append(y1)
        h.append(h1)
if len(x) == 1:
    print(x[0], y[0], h[0])
else:
    for cx, cy in itertools.product(range(101), repeat=2):
        ok = True
        H = h[0] + abs(x[0] - cx) + abs(y[0] - cy)
        for n in range(1, len(x)):
            ok &= h[n] + abs(x[n] - cx) + abs(y[n] - cy) == H
            if not ok:
                break
        if ok:
            break
    print(cx, cy, H)
