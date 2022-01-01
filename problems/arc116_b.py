N = int(input())
a = [int(_) for _ in input().split()]
a.sort()
mod = 998244353
ans = 0
val = a[N - 1]
ans += a[N - 1] * val
for i in range(N - 1, 0, -1):
    val = a[i] % mod + a[i - 1] % mod + 2 * (val - a[i]) % mod
    ans += val * a[i - 1] % mod
print(ans % mod)
