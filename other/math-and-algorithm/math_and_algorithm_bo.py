N, X, Y = [int(_) for _ in input().split()]
for a in range(1, N + 1):
    for b in range(a, N + 1):
        for c in range(b, N + 1):
            for d in range(c, N + 1):
                if a + b + c + d == X and a * b * c * d == Y:
                    exit(print("Yes"))
print("No")

