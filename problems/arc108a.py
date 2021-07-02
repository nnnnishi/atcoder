S, P = [int(_) for _ in input().split()]

N = P

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

for d in div:
    if (P // d) == S - d:
        exit(print("Yes"))

print("No")
