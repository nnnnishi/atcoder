# 耳dp
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/008.jpg
N = int(input())
S = list(input())
MOD = 998244353
dp = [[[0] * 10 for _ in range(2 ** 10)] for _ in range(N + 1)]
d = {}
i = 0
for s in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
    d[s] = i
    i += 1


def has_bit(n, i):
    return (n & 1 << i) > 0


# 場所
for i in range(1, N + 1):
    # i文字目x
    x = d[S[i - 1]]
    # 文字の集合
    for j in range(2 ** 10):
        for k in range(10):
            # 何もしないときもパターン数は引き継ぐ
            dp[i][j][k] = dp[i - 1][j][k]
            if k == x:
                # 直前とxが同じときは同じものを含むパターンを＋(2倍になる)
                dp[i][j][k] += dp[i - 1][j][k]
                dp[i][j][k] %= MOD
    for j in range(2 ** 10):
        if has_bit(j, x):
            continue
        # 含んでいなくて文字xを採用する
        for k in range(10):
            # 直前とxが違うとき同じものを含まないときにパターンを＋(2倍になる)
            dp[i][j | (1 << x)][x] += dp[i - 1][j][k]
            dp[i][j | (1 << x)][x] %= MOD
    # xだけ含むパターンに++
    dp[i][(1 << x)][x] += 1
    dp[i][(1 << x)][x] %= MOD

ans = 0
for j in range(2 ** 10):
    # 直前
    for k in range(10):
        if dp[N][j][k] != 0:
            ans += dp[N][j][k]
            ans %= MOD
print(ans)
