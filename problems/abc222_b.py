N, P = [int(_) for _ in input().split()]
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    if a[i] < P:
        ans += 1
print(ans)
