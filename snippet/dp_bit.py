# bitdp
# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_d

N = int(input())
S = list(input())


def has_bit(n, i):
    return (n & 1 << i) > 0


dp = [[0] * 8 for _ in range(2)]
d = {}
for i, c in enumerate(["J", "O", "I"]):
    d[c] = i

for n in range(1, 8):
    if has_bit(n, d["J"]) and has_bit(n, d[S[0]]):
        dp[0][n] = 1

MOD = 10007
ans = 0
for i in range(1, N):
    for nn in range(1, 8):
        # 初期化する
        dp[i % 2][nn] = 0
        for nb in range(1, 8):
            # 鍵をもつ
            for j in range(3):
                if has_bit(nn, j) and has_bit(nb, j) and has_bit(nn, d[S[i]]):
                    dp[i % 2][nn] += dp[(i + 1) % 2][nb]
                    dp[i % 2][nn] %= MOD
                    break
print(sum(dp[(N + 1) % 2]) % MOD)
