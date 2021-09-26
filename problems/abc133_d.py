N = int(input())
a = [int(_) for _ in input().split()]
tot = sum(a)
for i in range(1, N, 2):
    tot -= 2 * a[i]
ans = [tot]
for i in range(N - 1):
    ans.append(2 * a[i] - ans[i])

print(*ans)
