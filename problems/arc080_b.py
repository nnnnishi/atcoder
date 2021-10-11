import numpy as np

Y, X = [int(_) for _ in input().split()]
N = int(input())
a = [int(_) for _ in input().split()]
ans = np.zeros((Y, X))
n = 1
idx = 0
cnt = 0
while cnt < X * Y:
    y = cnt % Y
    x = cnt // Y
    if x % 2 == 0:
        ans[y][x] = n
    else:
        ans[Y - y - 1][x] = n
    a[idx] -= 1
    if a[idx] == 0:
        n += 1
        idx += 1
    cnt += 1


for y in range(Y):
    print(*map(int, list(ans[y])))

