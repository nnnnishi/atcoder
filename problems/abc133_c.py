L, R = [int(_) for _ in input().split()]
MOD = 2019
if R - L >= 2019:
    exit(print(0))
ans = 2018
for i in range(L, R):
    for j in range(i + 1, R + 1):
        ans = min(ans, i * j % MOD)
        if ans == 0:
            exit(print(0))
print(ans)
