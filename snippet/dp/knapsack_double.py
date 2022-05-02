# 複数回の選択をゆるすknapsack
# 利得Hを得るのに必要な重量の最小値Wを求める
# https://atcoder.jp/contests/abc153/tasks/abc153_e

H, N = [int(_) for _ in input().split()]

query = []
for _ in range(N):
    g, w = [int(_) for _ in input().split()]
    query.append([g, w])
INF = 10 ** 10
# dp[必要利得]= 必要重量
dp = [INF] * (H + 1)
dp[0] = 0

for g, w in query:
    for i in range(H + 1):
        if i <= g:
            # wより多く支払っているのであればwに更新
            dp[i] = min(dp[i], w)
        else:
            # 利得iの必要重量は、（もとのiの必要重量, (i-g)のときに支払っていた重量dp[i - g]+w）の小さい方
            dp[i] = min(dp[i], dp[i - g] + w)

print(dp[H])