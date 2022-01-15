N = int(input())
A = [int(_) for _ in input().split()]
dp = [0] * (N + 1)
for n in range(N):
    dp[n + 1] += max(dp[n], dp[n] + A[n])

print(dp[N])

