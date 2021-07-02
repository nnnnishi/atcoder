N = int(input())
a = [int(_) for _ in input().split()]
cnt = 0
ans = 1
for i in range(1, N):
    if a[i] - a[i - 1] > 0:
        cnt += 1
        ans += 1 + cnt
    else:
        ans += 1
        cnt = 0
print(ans)