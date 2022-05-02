N = int(input())
task = []
for _ in range(N):
    task.append([int(_) for _ in input().split()])
task.sort()
dmax = task[N - 1][0]
# dp[どの商品までか][日付] = 合計
dp = [[0] * (dmax + 1) for _ in range(N + 1)]
for i in range(N):
    for d in range(1, dmax + 1):
        dp[i + 1][d] = max(dp[i][d], dp[i + 1][d - 1])
        D, C, S = task[i][0], task[i][1], task[i][2]
        if d <= D and d >= C:
            dp[i + 1][d] = max(dp[i + 1][d], dp[i][d - C] + S)
# print(dp)
print(dp[N][dmax])
