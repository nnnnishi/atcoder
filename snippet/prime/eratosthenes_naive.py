N = int(input())
p = []
for i in range(2, N + 1):
    is_prime = 1
    for j in range(2, i):
        if i % j == 0:
            is_prime = 0
            break
    if is_prime:
        p.append(i)
print(*p)
