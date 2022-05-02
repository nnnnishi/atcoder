N = int(input())
A = [int(_) for _ in input().split()]
INF = 10 ** 10
dp = [[INF] * (2 * N) for _ in range(2 * N)]

# 隣り合う部分をまず計算
for i in range(2 * N - 1):
    dp[i][i + 1] = abs(A[i] - A[i + 1])

# 隣り合う部分の幅を決める
# 3個とばし、2つ間隔
for i in range(3, 2 * N + 1, 2):
    # 左側の位置をきめる
    for j in range(2 * N - i):
        # print("*", j)
        cl = j
        cr = j + i
        # 分割点をkとする
        for k in range(cl, cr - 1):
            # print(k, dp[cl][cr], dp[cl][k], dp[k][cr])
            dp[cl][cr] = min(dp[cl][cr], dp[cl][k] + dp[k + 1][cr])
        # 両端のものを取り除く場合（cl,crよりひとつ狭い部分+除くコスト）
        dp[cl][cr] = min(dp[cl][cr], dp[cl + 1][cr - 1] + abs(A[cl] - A[cr]))
    # print(dp)
    # print()
print(dp[0][2 * N - 1])
