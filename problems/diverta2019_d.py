N = int(input())

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
# print(div)
ans = 0

for d in div:
    if (N - d) // d > d:
        ans += (N - d) // d
print(ans)
