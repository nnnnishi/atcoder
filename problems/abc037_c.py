N, K = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
l = [0] * N
ans = 0
for i in range(N - K + 1):
    l[i] += 1
    if i + K < N:
        l[i + K] -= 1
for i in range(1, N):
    l[i] += l[i - 1]
for i in range(N):
    ans += a[i] * l[i]
print(ans)
