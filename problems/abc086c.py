N = int(input())
p = [[0, 0, 0]]
for i in range(N):
    p.append(list(map(int, input().split())))

ok = True
for i in range(N):
    t1, x1, y1 = p[i][0], p[i][1], p[i][2]
    t2, x2, y2 = p[i + 1][0], p[i + 1][1], p[i + 1][2]
    d = abs(x2 - x1) + abs(y2 - y1)
    dt = t2 - t1
    if d <= dt and dt % 2 == d % 2:
        continue
    ok = False
    break


if ok:
    print("Yes")
else:
    print("No")