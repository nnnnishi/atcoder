N, T = [int(_) for _ in input().split()]
t = [int(_) for _ in input().split()]

ans = 0
for i in range(N - 1):
    if t[i + 1] - t[i] <= T:
        ans += t[i + 1] - t[i]
    else:
        ans += T
ans += T
print(ans)