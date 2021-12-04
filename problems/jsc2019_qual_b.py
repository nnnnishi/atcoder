N, K = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

MOD = 10 ** 9 + 7
ans1 = 0
for i in range(N):
    for j in range(i + 1, N):
        if a[i] > a[j]:
            ans1 += 1

a = a * 2
ans2 = 0
for i in range(N):
    for j in range(N, N * 2):
        if a[i] > a[j]:
            ans2 += 1

print(((ans1 * K) + (ans2 * (K * (K - 1) // 2))) % MOD)

