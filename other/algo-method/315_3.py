# レーベンシュタイン距離
# https://algo-method.com/tasks/314/editorial

S = list(input())
T = list(input())
INF = 10 ** 5

lenS = len(S)
lenT = len(T)
dp = [[INF] * (lenT + 1) for _ in range(lenS + 1)]
dp[0][0] = 0
for i in range(lenS + 1):
    for j in range(lenT + 1):
        if i < lenS and j < lenT:
            if i - 1 >= 0 and j - 1 >= 0:
                if S[i - 1] == T[j - 1]:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
                    # print(i, j, dp[i + 1][j + 1], dp[i][j])
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + 1)
        if i < lenS:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
        if j < lenT:
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

# print(dp)
print(dp[lenS][lenT])
