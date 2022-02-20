N = int(input())
K = len(str(N))
M = 998244353
# まえのけたまでたす
ans = 0
for k in range(K - 1):
    kou = (10 ** (k + 1)) - (10 ** k)
    ans += ((((10 ** k) + ((10 ** (k + 1)) - 1))) * kou // 2) - kou * ((10 ** k) - 1)
    ans %= M
# そのけた
kou = N - (10 ** (K - 1)) + 1
ans += (((10 ** (K - 1)) + N) * kou // 2) - kou * ((10 ** (K - 1)) - 1)
ans %= M
print(ans)
