# 包除原理 (Inclusion-exclusion principl)
# D桁までのうち、N個のbit列といずれかが一致するXの総数を数える
# https://atcoder.jp/contests/typical90/tasks/typical90_cb
# https://twitter.com/e869120/status/1410368312760934404/photo/1

N, D = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
ans = pow(2, D)


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N
for n in range(1, 1 << N):
    cnt = 0
    x = 0
    for i in range(N):
        # Aiについてbitを足し合わせ
        if has_bit(n, i):
            x |= A[i]
    # print(x, bin(n))
    if bin(n).count("1") % 2 == 0:
        # D桁で、0の部分を0とするか1とするかのパターン数
        ans += pow(2, (D - bin(x).count("1")))
    else:
        ans -= pow(2, (D - bin(x).count("1")))

print(ans)
