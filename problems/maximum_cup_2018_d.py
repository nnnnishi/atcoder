N, M, L, X = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

dp = [[10 ** 6] * M for _ in range(N + 1)]
dp[0][0] = 0
ans = 0
for i in range(N):
    for m in range(M):
        dp[i + 1][(m + a[i]) % M] = min(
            dp[i][(m + a[i]) % M], dp[i][m] + (m + a[i]) // M
        )
# print(dp[N])
# print(L)
# print(dp[N][L])
if dp[N][L] < X:
    print("Yes")
else:
    print("No")
