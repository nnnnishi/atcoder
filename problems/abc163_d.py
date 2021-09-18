N, K = [int(_) for _ in input().split()]
MOD = 10 ** 9 + 7
ans = 0
for i in range(K, N + 2):
    ans += ((N + (N - i + 1)) * i // 2) - ((i - 1) * i // 2) + 1
    ans %= MOD
print(ans)
