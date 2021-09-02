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


K = int(input())
d = make_divisors(K)
D = len(d)
ans = 0
for i in range(D):
    if i ** 2 > K:
        break
    for j in range(i, D):
        if K / (d[i] * d[j]) < d[j]:
            break
        if K % (d[i] * d[j]) == 0:
            # print(d[i], d[j], K // (d[i] * d[j]))
            ans += 1
print(ans)