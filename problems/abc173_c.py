# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
Y, X, K = [int(_) for _ in input().split()]
c = []
for i in range(Y):
    c.append(list(input()))
ans = 0


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N
for ny in range(1 << Y):
    for nx in range(1 << X):
        # パターンnのi桁目が1 -> のこす
        cnt = 0
        for yi in range(Y):
            for xi in range(X):
                if has_bit(ny, yi) and has_bit(nx, xi):
                    if c[yi][xi] == "#":
                        cnt += 1
        # print(ny, nx, cnt)
        if cnt == K:
            ans += 1
print(ans)