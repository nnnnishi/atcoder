N = int(input())
l = []
for i in range(N):
    l.append([int(_) for _ in input().split()])
cnt = 0
for a, b in l[::-1]:
    if (a + cnt) % b == 0:
        continue
    else:
        cnt += b - ((a + cnt) % b)
print(cnt)
