p = set()
for i in range(2, 1000 + 1):
    is_prime = 1
    for j in range(2, i):
        if i % j == 0:
            is_prime = 0
            break
    if is_prime:
        p.add(i)

A, B, C, D = [int(_) for _ in input().split()]

for a in range(A, B + 1):
    ok = True
    for b in range(C, D + 1):
        if a + b in p:
            ok = False
            break
    if ok:
        print("Takahashi")
        exit()
print("Aoki")

