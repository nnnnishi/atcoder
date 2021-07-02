# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
S = input()
N = 3


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N
for n in range(1 << N):
    cnt = int(S[0])
    ans = S[0]
    # N桁
    for i in range(N):
        # パターンnのi桁目が1
        if has_bit(n, i):
            cnt += int(S[i + 1])
            ans += "+" + S[i + 1]
        else:
            cnt -= int(S[i + 1])
            ans += "-" + S[i + 1]

    if cnt == 7:
        exit(print(ans + "=7"))
