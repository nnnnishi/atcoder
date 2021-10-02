A = list(input())

# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える


def has_bit(n, i):
    return (n & 1 << i) > 0


N = len(A)
A.sort(reverse=True)
# N桁の0-1の組合せパターン数 1<<N

ans = 0
for n in range(1 << N):
    cnt = 0
    # N桁
    a = []
    b = []
    for i in range(N):
        # パターンnのi桁目が1
        if has_bit(n, i):
            a.append(A[i])
        else:
            b.append(A[i])
    # print(a, b)
    if len(a) == 0 or len(b) == 0 or a[0] == "0" or b[0] == "0":
        continue
    else:
        tmp = int("".join(a)) * int("".join(b))
        ans = max(tmp, ans)
        # print(tmp)
print(ans)
