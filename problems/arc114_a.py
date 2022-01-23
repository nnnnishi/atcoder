import math

M = int(input())
X = [int(_) for _ in input().split()]
cand = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def has_bit(n, i):
    return (n & 1 << i) > 0


ans = 10 ** 25
N = len(cand)
# N桁の0-1の組合せパターン数 1<<N
for n in range(1, 1 << N):
    # N桁
    a = 1
    for i in range(N):
        # パターンnのi桁目が1
        if has_bit(n, i):
            a *= cand[i]
    ok = True
    for t in range(M):
        if math.gcd(X[t], a) == 1:
            ok = False

    if ok and a < ans:
        ans = a
print(ans)
