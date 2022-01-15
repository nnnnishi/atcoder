# 個数制限付き部分和問題
# whileっぽい処理がはいるもの
# O(NM)
# https://algo-method.com/tasks/313/editorial
import sys

input = sys.stdin.readline
INF = 10 ** 10
N, M = [int(_) for _ in input().split()]
A = []
B = []
for _ in range(N):
    a, b = [int(_) for _ in input().split()]
    A.append(a)
    B.append(b)

dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        # 3パターンのいずれかの最小値をみればよい（Mの判定のため最小値）
        # パターン1: iまででjがでていたら0で初期化
        if dp[i][j] != INF:
            dp[i + 1][j] = 0
        if j >= A[i]:
            # パターン2: iまでで -A[i] したところにでていたら1に設定
            if dp[i][j - A[i]] < INF:
                dp[i + 1][j] = min(dp[i + 1][j], 1)
            # パターン3: i+1で -A[i] したところででていたら+1
            if dp[i + 1][j - A[i]] < B[i]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - A[i]] + 1)

if dp[N][M] != INF:
    print("Yes")
else:
    print("No")
