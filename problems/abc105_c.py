# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
inN = int(input())
N = 16
ans = ""


def has_bit(n, i):
    return (n & 1 << i) > 0


dpos = {}
dpos_inv = {}
# 正の数を準備
# N桁の0-1の組合せパターン数 1<<N
for n in range(1 << N):
    cnt = 0
    # N桁
    for i in range(N):
        # パターンnのi桁目が1
        if has_bit(n, i):
            cnt += 4 ** i
    dpos[n] = cnt
    dpos_inv[cnt] = n

# 負の数
for n in range(1 << N):
    cnt = 0
    # N桁
    for i in range(N):
        # パターンnのi桁目が1
        if has_bit(n, i):
            cnt += -2 * (4 ** i)
    if inN - cnt in dpos_inv:
        posb = []
        negb = []
        for j in range(N):
            # パターンnのi桁目が1
            if has_bit(n, j):
                negb.append("1")
            else:
                negb.append("0")
        for j in range(N):
            # パターンnのi桁目が1
            if has_bit(dpos_inv[inN - cnt], j):
                posb.append("1")
            else:
                posb.append("0")
        for k, l in zip(posb, negb):
            ans += k + l
        print(int(ans[::-1]))