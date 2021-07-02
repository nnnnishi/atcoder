X, Y = [int(_) for _ in input().split()]
if (X + Y) % 3 != 0:
    exit(print(0))
AB = (X + Y) // 3
if (2 * X - Y) % 3 != 0:
    exit(print(0))
A = (2 * X - Y) // 3
B = (2 * Y - X) // 3
if Y > 2 * X or X > 2 * Y:
    exit(print(0))


def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    # 分子
    numerator = [n - r + k + 1 for k in range(r)]
    # 分母
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


if A >= 0:
    print(cmb(AB, A) % (10 ** 9 + 7))
else:
    print(cmb(AB, B) % (10 ** 9 + 7))
