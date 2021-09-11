N = int(input())
a = [int(_) for _ in input().split()]
a.sort()

ans = 0
for i in range(N - 1):
    if 2 * a[i] >= a[i + 1]:
        ans += 1
        a[i + 1] += a[i]
    else:
        ans = 0
        a[i + 1] += a[i]
print(ans + 1)
