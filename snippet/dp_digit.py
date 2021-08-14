# https://atcoder.jp/contests/tdpc/tasks/tdpc_number
# 類題：https://atcoder.jp/contests/abc029/tasks/abc029_d
D = int(input())
N = input()
nl = list(N)
n = len(N)
MOD = 10 ** 9 + 7
# dp[けた:i][smaller:0,1][桁和のmod:j] = パターン数, 配列作成 O(keta*2*D)
# 3つめをうまく設定する
dp = []
for i in range(n + 1):
    dp.append([])
    for s in range(2):
        dp[i].append([])
        for j in range(D):
            dp[i][s].append(0)

# 初期状態から遷移するのでどこかに1がたつ
dp[0][0][0] = 1

# dp
for i in range(n):
    nint = int(nl[i])
    for j in range(D):
        # i桁目がsmaller=1 -> ちいさいのでi+1桁目の値kはなんでもOK
        for k in range(10):
            dp[i + 1][1][(j + k) % D] += dp[i][1][j]
            dp[i + 1][1][(j + k) % D] %= MOD
        # i桁目がsmaller=0(Nとおなじ) -> i+1桁目もNとおなじか、Nより小さいかで場合分け
        # i+1桁目はNよりちいさい:dp[i+1][1]
        for k in range(nint):
            dp[i + 1][1][(j + k) % D] += dp[i][0][j]
            dp[i + 1][1][(j + k) % D] %= MOD
        # i+1桁目もNとおなじ:dp[i+1][0]
        dp[i + 1][0][(j + nint) % D] = dp[i][0][j] % MOD
# print(dp)
print((dp[n][0][0] + dp[n][1][0] - 1) % MOD)
