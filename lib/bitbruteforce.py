# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
N = 16
M = 1
ans = 0


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N
for n in range(1 << N):
    cnt = 0
    # N桁
    for i in range(N):
        # パターンnのi桁目が1
        if has_bit(n, i):
            cnt += 1
    if cnt == M:
        ans += 1
print(ans)