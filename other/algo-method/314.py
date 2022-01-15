# 最長共通部分列 Longest Common String (LCS)
# https://algo-method.com/tasks/314/editorial
S = list(input())
T = list(input())
lenS = len(S)
lenT = len(T)
# dp[i+1][j+1]: Sのi文字目、Tのj文字目までのLCSの文字数
dp = [[0] * (lenT + 1) for _ in range(lenS + 1)]

for i in range(lenS):
    for j in range(lenT):
        if S[i] != T[j]:
            # 文字が一致しない -> （Sのi-1文字目、Tのj文字目）、（Sのi文字目、Tのj-1文字目）の大きい方から変化なし
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        else:
            # (Sのi-1文字目、Tのj-1文字目)+1
            dp[i + 1][j + 1] = dp[i][j] + 1
# print(dp)
print(dp[lenS][lenT])
