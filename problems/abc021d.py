n = int(input())
k = int(input())

ans = 1
tmp = 1
mod = 10 ** 9 + 7
for i in range(2, n + 1):
    tmp = ((tmp % mod) * ((k - 2 + i) % mod)) * pow(i - 1, mod - 2, mod)
    ans += tmp % mod
    ans = ans % mod
print(ans)
