A, B = [int(_) for _ in input().split()]
# Bまでにふくまれているかず - A-1までにふくまれているかず


def check(N):
    N = str(N)
    nl = list(N)
    n = len(N)
    # dp[けた:i][smaller:0,1][0-9のどれか] = パターン数, 配列作成 O(keta*2*2)
    dp = []
    for i in range(n + 1):
        dp.append([])
        for s in range(2):
            dp[i].append([])
            for j in range(2):
                dp[i][s].append(0)
    # 0桁目が0は4,9をふくまない
    dp[0][0][0] = 1

    # dp
    for i in range(n):
        nint = int(nl[i])
        # i桁目がsmaller=1 -> ちいさいのでi+1桁目の値kはなんでもOK
        for k in range(10):
            if k == 4 or k == 9:
                dp[i + 1][1][1] += dp[i][1][0] + dp[i][1][1]
            else:
                dp[i + 1][1][1] += dp[i][1][1]
                dp[i + 1][1][0] += dp[i][1][0]
        # i桁目がsmaller=0(Nとおなじ) -> i+1桁目もNとおなじか、Nより小さいかで場合分け
        # i+1桁目はNよりちいさい:dp[i+1][1]
        for k in range(nint):
            if k == 4 or k == 9:
                # i+1でsmallerでふくむ、iけためまでで含む or iけためまでにふくまない
                dp[i + 1][1][1] += dp[i][0][0] + dp[i][0][1]
            else:
                # i+1でsmallerでふくまない、iけためまでで含まなく、i+1でもふくまない
                dp[i + 1][1][1] += dp[i][0][1]
                dp[i + 1][1][0] += dp[i][0][0]
        # i+1桁目もNとおなじ:dp[i+1][0]
        if nint == 4 or nint == 9:
            # i+1でsmallerでなく、iけためまでで含む or iけためまでにふくまない
            dp[i + 1][0][1] += dp[i][0][0] + dp[i][0][1]
        else:
            # i+1でsmallerでなく、iけためまでにふくまない
            dp[i + 1][0][1] += dp[i][0][1]
            dp[i + 1][0][0] += dp[i][0][0]
    # print(dp)
    # print(dp[n][1][1] + dp[n][0][1])
    return dp[n][1][1] + dp[n][0][1]


print(check(B) - check(A - 1))
