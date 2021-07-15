N, M = [int(_) for _ in input().split()]
l = []
for i in range(N):
    l.append([int(_) for _ in input().split()])
l.sort()

ans = 0
for li in l:
    if li[1] <= M:
        ans += li[0] * li[1]
        M -= li[1]
    else:
        ans += li[0] * M
        break
print(ans)