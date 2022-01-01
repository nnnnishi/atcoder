N, S = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
# dp[合計]=  パターン数
dp = [0] * (S + 1)
dp[0] = 1

for n in range(N):
    dp_pre = dp.copy()
    dp = [0] * (S + 1)
    for i in range(S + 1):
        if dp_pre[i] > 0:
            dp[i] = dp_pre[i]
            if i + A[n] <= S:
                dp[i + A[n]] += dp_pre[i]
if dp[S] > 0:
    print("Yes")
else:
    print("No")
