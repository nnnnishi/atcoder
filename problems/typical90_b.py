# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
N = int(input())
if N % 2 != 0:
    exit(print())


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N
ans = []
for n in range(1 << N):
    cnt = 0
    t = ""
    # N桁
    for i in range(N):
        # パターンnのi桁目が1
        if has_bit(n, i):
            cnt += 1
            t += "("
        else:
            cnt -= 1
            t += ")"
        if cnt < 0:
            break
    if i == N - 1 and cnt == 0:
        ans.append(t)
ans.sort()
for a in ans:
    print(a)