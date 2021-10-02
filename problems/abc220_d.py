N = int(input())
a = list(map(int, input().split()))
ans = [0] * 10

MOD = 998244353

dp = [[0] * 10 for _ in range(N)]
dp[0][a[0]] = 1
for i in range(1, N):
    for j in range(10):
        dp[i][(a[i] * j) % 10] += dp[i - 1][j]
        dp[i][(a[i] * j) % 10] %= MOD
        dp[i][(a[i] + j) % 10] += dp[i - 1][j]
        dp[i][(a[i] + j) % 10] %= MOD

for i in range(10):
    print(dp[N - 1][i])
