N = int(input())
a = [int(_) for _ in input().split()]
a.sort(reverse=True)
ans = 0
for i in range(1, 2 * N, 2):
    ans += a[i]
print(ans)