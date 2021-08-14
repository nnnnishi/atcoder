N = int(input())
a = [int(_) for _ in input().split()]


def has_bit(n, i):
    return (n & 1 << i) > 0


mod = 10 ** 9 + 7
ans = 0
for d in range(60):
    zero = 0
    one = 0
    for ai in a:
        if has_bit(ai, d):
            one += 1
        else:
            zero += 1
    ans += (one * zero) * pow(2, d) % mod
print(ans % mod)
