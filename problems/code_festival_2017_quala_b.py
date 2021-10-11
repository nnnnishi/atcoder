Y, X, K = [int(_) for _ in input().split()]

for y in range(Y + 1):
    for x in range(X + 1):
        if y * X - 2 * x * y + Y * x == K:
            exit(print("Yes"))
print("No")

