N = int(input())
r = []
b = []
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    r.append([x, y])
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    b.append([x, y])

r.sort(key=lambda x: (-x[1], x[0]))
b.sort(key=lambda x: (x[0], -x[1]))

used = set()
ans = 0
for j in range(N):
    for i in range(N):
        if i not in used and r[i][0] < b[j][0] and r[i][1] < b[j][1]:
            ans += 1
            used.add(i)
            break
print(ans)