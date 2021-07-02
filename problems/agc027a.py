N, x = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
a.sort()
ans = 0
for i in range(N - 1):
    if x >= a[i]:
        ans += 1
        x -= a[i]
    else:
        exit(print(ans))
if x == a[N - 1]:
    print(ans + 1)
else:
    print(ans)