N = int(input())
a = [int(_) for _ in input().split()]
l = 0
ans = 0
for i in range(N - 1):
    if a[i + 1] <= a[i]:
        l += 1
    else:
        ans = max(l, ans)
        l = 0
ans = max(l, ans)
print(ans)