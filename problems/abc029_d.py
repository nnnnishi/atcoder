N = input()
nl = list(N)
n = len(N)
# dp[けた:i][smaller:0,1][1の個数] = パターン数, 配列作成 O(keta*2*D)
dp = []
for i in range(n + 1):
    dp.append([])
    for s in range(2):
        dp[i].append([])
        for j in range(10):
            dp[i][s].append(0)

dp[0][0][0] = 1
c = 0
# dp
for i in range(n):
    nint = int(nl[i])
    for j in range(9):
        # i桁目がsmaller=1 -> ちいさいのでi+1桁目の値kはなんでもOK
        for k in range(10):
            if k == 1:
                dp[i + 1][1][j + 1] += dp[i][1][j]
            else:
                dp[i + 1][1][j] += dp[i][1][j]
        # i桁目がsmaller=0(Nとおなじ) -> i+1桁目もNとおなじか、Nより小さいかで場合分け
        # i+1桁目はNよりちいさい:dp[i+1][1]
        for k in range(nint):
            if k == 1:
                dp[i + 1][1][j + 1] += dp[i][0][j]
            else:
                dp[i + 1][1][j] += dp[i][0][j]
        # i+1桁目もNとおなじ:dp[i+1][0]
        if nint == 1:
            dp[i + 1][0][j + 1] += dp[i][0][j]
        else:
            dp[i + 1][0][j] = dp[i][0][j]

print(sum([(j * dp[n][0][j] + j * dp[n][1][j]) for j in range(1, 10)]))
