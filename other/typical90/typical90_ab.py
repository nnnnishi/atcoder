N = int(input())
a = [[0] * 1001 for i in range(1001)]
ymax = 0
xmax = 0
for _ in range(N):
    lx, ly, rx, ry = [int(_) for _ in input().split()]
    a[ly][lx] += 1
    a[ly][rx] -= 1
    a[ry][lx] -= 1
    a[ry][rx] += 1
    ymax = max(ry + 1, ymax)
    xmax = max(rx + 1, xmax)

for y in range(1001):
    for x in range(1, 1001):
        a[y][x] = a[y][x] + a[y][x - 1]
for x in range(1001):
    for y in range(1, 1001):
        a[y][x] = a[y][x] + a[y - 1][x]
"""
print("*" * 20)
for y in range(ymax):
    print(a[y][:xmax])
print("*" * 20)
"""
ans = [0] * (N + 1)
for x in range(1001):
    for y in range(1001):
        ans[a[y][x]] += 1
for i in range(1, N + 1):
    print(ans[i])