N = int(input())
c = list(map(int, input().split()))
ans = 1
MOD = (10 ** 9) + 7
c.sort()
for i in range(N):
    ans *= c[i] - i
    ans %= MOD
print(ans)
