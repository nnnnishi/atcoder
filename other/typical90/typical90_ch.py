N, Q = [int(_) for _ in input().split()]
d_max = 60
query = []
for i in range(Q):
    query.append([int(_) for _ in input().split()])

b = [[1] * d_max for _ in range(N)]


def has_bit(n, i):
    return (n & 1 << i) > 0


# bをつくる
for q in query:
    x, y, z, w = q
    # N桁
    for i in range(d_max):
        # パターンnのi桁目が1
        if not has_bit(w, i):
            b[x - 1][i] = 0
            b[y - 1][i] = 0
            b[z - 1][i] = 0
# for i in range(N):
#    print(b[i])
ans = 1
# bitごとにすべてのパターンを満たす数を数える
for d in range(d_max):
    # Nこの数字の0-1パターンで整合するものの数cnt
    cnt = 0
    for n in range(1 << N):
        ok = 1
        for i in range(N):
            # パターンでその数字をつかえるか
            if has_bit(n, i) and b[i][d] != 1:
                ok = 0
                break
        if ok:
            if d == 60:
                print(n)
            for q in query:
                x, y, z, w = q
                # wのd桁目が1ならばどれかが1
                if has_bit(w, d):
                    if not (
                        has_bit(n, x - 1) or has_bit(n, y - 1) or has_bit(n, z - 1)
                    ):
                        ok = 0
                        break
        if ok:
            cnt += 1

    # 桁ごとのパターン数を乗ずる
    ans *= cnt
    ans %= 10 ** 9 + 7

print(ans)
