N = int(input())
a = [int(_) for _ in input().split()]
cnt = 1
ans = 0
ok = False
for i in range(N):
    if a[i] == cnt:
        ok = True
        cnt += 1
    else:
        ans += 1
if ok:
    print(ans)
else:
    print(-1)
