N = int(input())
A = [int(_) for _ in input().split()]
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = A[0]
    elif i == 1:
        dp[i] = max(A[1], A[0])
    else:
        dp[i] = max(dp[i - 1], A[i] + dp[i - 2])

print(dp[N - 1])

