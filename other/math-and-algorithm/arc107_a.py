a, b, c = [int(_) for _ in input().split()]
M = 998244353
ans = 1
ans *= ((1 + a) * a // 2) % M
ans %= M
ans *= ((1 + b) * b // 2) % M
ans %= M
ans *= ((1 + c) * c // 2) % M
ans %= M
print(ans)

