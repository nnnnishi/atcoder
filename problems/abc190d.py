N = int(input())

div_low = []
div_high = []
for i in range(1, 2 * N + 1):
    if i * i > 2 * N:
        break
    if (2 * N) % i == 0:
        div_low.append(i)
        if i != 2 * N // i:
            div_high.append(2 * N // i)

div = div_low + div_high[::-1]
# print(div)
ans = 0

for d in div:
    if ((2 * N) // d - (d - 1)) % 2 == 0:
        ans += 1
print(ans)
