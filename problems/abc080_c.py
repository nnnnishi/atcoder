# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
N = int(input())
F = {}
P = {}
# 0-N-1, (2*j)+k
for i in range(N):
    F[i] = [int(_) for _ in input().split()]
for i in range(N):
    P[i] = [int(_) for _ in input().split()]
ans = 0


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N
ans = -(10 ** 30)
for n in range(1, 1 << 10):
    cnt = 0
    # 10桁, (2*j)+k
    for i1 in range(N):
        eig = 0
        for i in range(10):
            # パターンnのi桁目が1
            if has_bit(n, i):
                eig += F[i1][i]
        cnt += P[i1][eig]
    ans = max(ans, cnt)
print(ans)