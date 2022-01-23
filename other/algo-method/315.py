# レーベンシュタイン距離
# https://algo-method.com/tasks/314/editorial

S = list(input())
T = list(input())
INF = 10 ** 5

lenS = len(S)
lenT = len(T)
dp = [[INF] * (lenT + 1) for _ in range(lenS + 1)]
dp[0][0] = 0
for i in range(-1, lenS):
    for j in range(-1, lenT):
        if i == -1 and -1 == 0:
            continue
        if i >= 0 and j >= 0:
            if S[i] == T[j]:
                dp[i + 1][j + 1] = dp[i][j]
            else:
                dp[i + 1][j + 1] = dp[i][j] + 1
        if i >= 0 and dp[i][j + 1] + 1 < dp[i + 1][j + 1]:
            dp[i + 1][j + 1] = dp[i][j + 1] + 1
        if j >= 0 and dp[i + 1][j] + 1 < dp[i + 1][j + 1]:
            dp[i + 1][j + 1] = dp[i + 1][j] + 1

# print(dp)
print(dp[lenS][lenT])
