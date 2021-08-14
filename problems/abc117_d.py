N, K = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]


def has_bit(n, i):
    return (n & 1 << i) > 0


if K == 0:
    exit(print(sum(a)))

d = 40  # 2^40 > 10^12

# イコール、未満
dp = [[0] * 2 for _ in range(d + 1)]
flag = False
for i in range(d):
    pow2 = pow(2, d - i - 1)
    # 0になるかず
    zero = sum(not (ai & pow2) for ai in a)
    # 1になるかず
    one = N - zero

    if K & pow2:
        if flag:
            dp[i + 1][1] = max(dp[i][0] + one * pow2, dp[i][1] + max(one, zero) * pow2)
        else:
            dp[i + 1][1] = dp[i][0] + one * pow2
            flag = True
        dp[i + 1][0] = dp[i][0] + zero * pow2
    else:
        if flag:
            dp[i + 1][1] = dp[i][1] + max(one, zero) * pow2
        dp[i + 1][0] = dp[i][0] + one * pow2

print(max(dp[d][0], dp[d][1]))