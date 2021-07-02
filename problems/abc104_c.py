# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
N, G = [int(_) for _ in input().split()]
A = []
for i in range(N):
    A.append([int(_) for _ in input().split()])
ans = 10 ** 10


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N
for n in range(1 << N):
    cnt = 0
    s = 0
    check = set()
    # N桁
    for i in range(N):
        # パターンnのi桁目が1, ぜんぶとく
        if has_bit(n, i):
            cnt += A[i][0]
            s += (i + 1) * 100 * A[i][0] + A[i][1]
            check.add(i)
    if s >= G:
        ans = min(cnt, ans)
    else:
        for i in range(N - 1, -1, -1):
            if i not in check:
                for j in range(A[i][0] - 1):
                    cnt += 1
                    s += (i + 1) * 100
                    if s >= G:
                        ans = min(cnt, ans)
                        break
print(ans)