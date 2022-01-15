# 最小コスト弾性マッチング問題
# https://algo-method.com/tasks/316/editorial
N, M = [int(_) for _ in input().split()]
C = [[int(_) for _ in input().split()] for _ in range(N)]
INF = 10 ** 10

dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M):
        if i - 1 <= N and j + 1 <= M:
            # dp[i+1][j+1]: AiとBjまでの弾性コスト
            dp[i + 1][j + 1] = min(
                dp[i + 1][j + 1],
                dp[i][j + 1] + C[i][j],
                dp[i + 1][j] + C[i][j],
                # dp[i][j+1]: A(i-1)とB(j-1)までの弾性コストにAi,Bjをたす
                dp[i][j] + C[i][j],
            )

print(dp)
print(dp[N][M])
