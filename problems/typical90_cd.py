l, r = [int(_) for _ in input().split()]
mae2 = 0
ato2 = 0
M = 10 ** 9 + 7
i = 1
if l - 1 < 10 ** i:
    mae2 += (l - 1) * l * pow(2, -1, M)
else:
    mae2 += 9 * 10 * pow(2, -1, M)
    for i in range(2, 20):
        if l - 1 >= 10 ** i - 1:
            mae2 += (
                (
                    (10 ** i - 1) % M * (10 ** i) % M * pow(2, -1, M)
                    - (10 ** (i - 1) - 1) % M * ((10 ** (i - 1))) % M * pow(2, -1, M)
                )
                * i
            ) % M

        else:
            mae2 += (
                (
                    (l - 1) % M * ((l - 1) + 1) % M * pow(2, -1, M)
                    - (10 ** (i - 1) - 1) % M * (10 ** (i - 1)) % M * pow(2, -1, M)
                )
                * i
            ) % M
            break


i = 1
if r < 10 ** i:
    ato2 += r * (r + 1) * pow(2, -1, M)
else:
    ato2 += 9 * 10 * pow(2, -1, M)
    for i in range(2, 20):
        if r >= 10 ** i - 1:
            ato2 += (
                (
                    (10 ** i - 1) % M * (10 ** i) % M * pow(2, -1, M)
                    - (10 ** (i - 1) - 1) % M * (10 ** (i - 1)) % M * pow(2, -1, M)
                )
                * i
            ) % M

        else:
            ato2 += (
                (
                    r % M * (r + 1) % M * pow(2, -1, M)
                    - (10 ** (i - 1) - 1) % M * (10 ** (i - 1)) % M * pow(2, -1, M)
                )
                * i
            ) % M
            break
print((ato2 - mae2) % M)
