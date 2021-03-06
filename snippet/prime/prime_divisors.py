# 約数列挙
def make_divisors(N):
    div_low = []
    div_high = []
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i == 0:
            div_low.append(i)
            if i != N // i:
                div_high.append(N // i)

    div = div_low + div_high[::-1]
    return div


print(make_divisors(10 ** 8))
print(len(make_divisors(10 ** 8)))